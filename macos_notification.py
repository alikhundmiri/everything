import os

# def notify(title, text):
# 	os.system("""
# 		osascript -e 'display notification "{}" with title "{}"'
# 		""".format(text, title))
	
# 	os.system("""
# 		osascript -e 'set theDialogText to "{}" & (current date) & "."
# display dialog theDialogText'
# 		""").format(title)



def notify(title, text):

	os.system("""
		osascript -e 'display dialog "How old are you?" buttons {"Open", "Close"}'
		""")

	'''
	if button returned:Open
		then open web browser with gmail opened
	'''



notify("Tution Advert Posted", "Please Check your email.")

