
def compound_interest(principle, rate, time): 
	new_amount = principle * (pow((1 + rate / 100), time)) 
	return(round(new_amount))

if __name__ == '__main__':
	principle = 10000
	rate = 13
	time = 10
	amount = compound_interest(principle, rate, time)

	print("\nAfter {} years, with {} rate, This is your Wealth Gain \n".format(time, rate))
	print("Amount Invested : {}".format(principle))
	print("Wealth Gain \t: {}".format(int(amount)-principle))
	print("___________________")
	print("Total Amount\t: {}".format(amount))
	print("___________________")
