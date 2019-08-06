import sys
import nltk
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup



def get_header(metas):
	# Find the Keywords, and remove stop words using nltk library
	description = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
	keywords = list(description[0].split(" "))
	# set english stop words, and remove them
	stop_words = list(stopwords.words('english'))
	for keyword in keywords:
		if keyword in stop_words:
			keywords.remove(keyword)

	return keywords


def get_details(keywords, h1_tags_text, h2_tags_text, p_tags_text):
	h1_score = []
	h2_score = []
	p_score = []

	for keyword in keywords:
		h1_score_ = 0
		for tag in h1_tags_text:
			if keyword in tag:
				h1_score_ += 1
		h1_score.append(h1_score_)

		h2_score_ = 0
		for tag in h2_tags_text:
			if keyword in tag:
				h2_score_ += 1
		h2_score.append(h2_score_)

		p_score_ = 0
		for tag in h1_tags_text:
			if keyword in tag:
				p_score_ += 1
		p_score.append(p_score_)

	return h1_score, h2_score, p_score

def get_tag_text(tags):
	list_tags = []
	for tag in tags:
		list_tags.append(tag.get_text(separator=' '))
	return list_tags

def print_results(url, keywords, h1_score, h2_score, p_score):		
	print("\nResults for webpage: {}".format(url))
	print("{} \t| {} - {} - {} | {}".format("#", "h1", "h2", "p", "keyword"))
	print("__________________________")
	for i, (keyword, h1, h2, p) in enumerate(zip(keywords, h1_score, h2_score, p_score)):
		print("{} \t| {} - {} - {} | {}".format(i, h1, h2, p, keyword))
	print("__________________________\n")


def start(url):
	response = ''
	try:
		response = requests.get(url)
	except requests.exceptions.MissingSchema as e:
		print("oops, you forgot the https/http in your input. Nevermind...")
		new_url = "https://" + url
		start(new_url)

	try:
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		# Whoops it wasn't a 200
		print("Error: " + str(e))
		return False

	soup = BeautifulSoup(response.text, "lxml")
	metas = soup.find_all('meta')
	h1_tags = soup.find_all('h1')
	h2_tags = soup.find_all('h2')
	p_tags = soup.find_all('p')

	# get plaintext from tags
	h1_tags_text = get_tag_text(h1_tags)
	h2_tags_text = get_tag_text(h2_tags)
	p_tags_text = get_tag_text(p_tags)

	# get keywords
	keywords = get_header(metas)
	# count keyword occurance in H1, H2, and P tags
	h1_score, h2_score, p_score = get_details(keywords, h1_tags_text, h2_tags_text, p_tags_text)
	# print the results
	print_results(url, keywords, h1_score, h2_score, p_score)

	return True


if __name__ == '__main__':
	default_link = ''

	if len(sys.argv) > 1:
		default_link = sys.argv[1]

	elif len(sys.argv) == 1:
		default_link = 'http://ardizen.com/landing-page/experience-art-investment.html'

	start(default_link)