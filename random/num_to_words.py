# pip install inflect, thats the library we are using
import sys, inflect

def say_the_words(num):
	p = inflect.engine()
	string_ = p.number_to_words(num)

	return(string_)

if __name__ == '__main__':
	
	int_num = input("Please enter a number: ")
	str_num = say_the_words(int_num)
	print(str_num)