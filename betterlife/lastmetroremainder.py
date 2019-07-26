import os
import requests
import datetime
import webbrowser
from datetime import timedelta
import time

office_ips = [
	'223.230.66.40',
	'183.82.107.34',
]

last_train_time = datetime.time(21, 42, 00)
warning_video = 'https://www.youtube.com/watch?v=CduA0TULnow'

url = 'https://jsonip.com/'

def get_ip():
	r = requests.get(url)
	response = r.json()
	current_ip = response['ip']
	if current_ip in office_ips:
		current_time = datetime.datetime.now().time()
		print("Its {} and you are in office with ip address: {}".format(current_time, current_ip))
		last_train_in = datetime.datetime.combine(datetime.date.today(), last_train_time) - datetime.datetime.combine(datetime.date.today(), current_time)

		days	= divmod(last_train_in.seconds, 86400)		# Get days
		hours 	= divmod(days[1], 3600)						# Use remainder of days to calc hours
		minutes	= divmod(hours[1], 60)						# Use remainder of hours to calc minutes

		time_remaining = "{} hours {} minutes".format(hours[0], minutes[0])
		print(minutes[0])
		if hours[0] == 0 and minutes[0] < 30:
			webbrowser.open(warning_video)
			notify("Travel Time: 45 Minutes", "You have {} before last train leaves".format(time_remaining), "Alert | Last Metro Remainder", 'Sosumi')

		else:	
			notify("Travel Time: 45 Minutes", "You have {} before last train leaves".format(time_remaining), "Last Metro Remainder", 'Hero')

	else:
		print("You are not in office")


def notify(title, text, subtitle, Audio):
    if subtitle:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'
        """.format(title, subtitle, text, Audio))
    else:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" sound name "{}"'
        """.format(title, text, Audio))

if __name__ == '__main__':
	time.sleep(5)
	get_ip()