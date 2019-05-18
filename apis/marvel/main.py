import os, json, time, hashlib, requests

WRITE_OUTPUT = False

marvel_public_key = os.environ.get('marvel_public_key')
marvel_private_key = os.environ.get('marvel_private_key')

BASE_URL = 'http://gateway.marvel.com/'

def generate_hash(ts):
	string = str(ts) + marvel_private_key + marvel_public_key
	hash_string = hashlib.md5(string.encode())
	return hash_string.hexdigest()

def write_file(json_response):
	file = open("stories.txt", "w")
	file.write(json_response)
	file.close()

def main():
	RequestUrl = 'http://gateway.marvel.com/v1/public/characters'
	ts = str(time.time()).replace('.','')
	unique_hash = generate_hash(ts)
	Params = {
		"apikey": marvel_public_key,
		"ts": ts,
		"hash": unique_hash,
	}
	Headers: {
		Accept: "*/*"
	}

	r = requests.get(url=RequestUrl, params=Params)
	json_data = json.loads(r.text)
	json_response = json.dumps(json_data, indent=4, sort_keys=True)

	if WRITE_OUTPUT:
		write_file(json_response)

	for response in json_data['data']['results']:
		# print(response)
		for next_ in response['events']['items']:
			print(next_['name'])

# def read_json_test():
# 	# file = open("response.txt", "w").read()
# 	# json_data = json.loads(file)
# 	# print(json_data)
# 	# file.close()
# 	json_data = ''
# 	with open('response.txt', 'r') as f:
# 		json_data = json.load(f)
	
# 	# print(json_data['data']['results'])
# 	for response in json_data['data']['results']:
# 		# print(response)
# 		for next_ in response['characters']:
# 			for then_some in next_:
# 				print(then_some['item'])

if __name__ == '__main__':
	main()
	# read_json_test()