import math

def main(x,y):
	multiply = 0
	fact = 0

	try:
		multiply = x*y
	except Exception as e:
		print(e)
	else:
		fact = math.factorial(multiply)
	finally:
		print("the factorial of Product of {} and {} is {}".format(x,y,fact))
if __name__ == '__main__':
	main(2,3)