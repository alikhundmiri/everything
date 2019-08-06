import single_link

links = [
'http://ardizen.com/landing-page/experience-art-investment.html',
'http://ardizen.com/landing-page/new-artist-investment.html',
'http://ardizen.com/landing-page/corporate-office.html',
'http://ardizen.com/landing-page/reception.html',
'http://ardizen.com/landing-page/waiting-room.html',
'http://ardizen.com/landing-page/gift-colleague.html',
'http://ardizen.com/landing-page/start-investing-in-art.html',
'http://ardizen.com/landing-page/new-art-investment.html',
'http://ardizen.com/landing-page/index.html',

]
def main():
	print("_____________________________\n")
	for link in links:
		single_link.start(link)
	print("_____________________________\n")

if __name__ == '__main__':
	main()