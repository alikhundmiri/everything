from time import gmtime, strftime
file_location = "location/to/file.txt"

def log_error(error_message):
	hs = open(file_location,"a")
	date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	message = date + " " error_message
	hs.write(message)
	hs.close() 	

# 2009-01-05 22:14:39 error on line 43
if __name__ == '__main__':
	log_error(error_message)