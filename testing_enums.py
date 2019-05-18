class MathClass(): 

	n1, n2 = 58, 40
	
	addition = n1 + n2
	division = n1/n2
	difference = n1 - n2
	
if __name__ == '__main__':
	print("Addition: {}".format(MathClass.addition))
	print("Division: {}".format(MathClass.division))
	print("Difference: {}".format(MathClass.difference))