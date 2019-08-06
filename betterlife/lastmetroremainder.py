import os, sys
import requests
import datetime
import webbrowser
from datetime import timedelta
import time

office_ips = [
	'223.230.66.40',
	'183.82.107.34',
]

last_train_time = datetime.time(22, 00, 00)
warning_video = 'https://www.youtube.com/watch?v=CduA0TULnow'

url = 'https://jsonip.com/'

walk_office_to_metro = 5
metro_wait_average = 3
metro_ride_1 = 8
metro_ride_2 = 22
walk_metro_to_home = 20



def log_file(message):
	file_name = '{}/lastmetroreminder_{}.txt'.format(os.path.dirname(sys.argv[0]),'{:02d}'.format(datetime.date.today().month))
	with open(file_name,"a+") as f:
		f.write(message)

def get_ip():
	r = requests.get(url)
	response = r.json()
	current_ip = response['ip']
	if current_ip in office_ips:
		date_today = datetime.date.today()
		current_time = datetime.datetime.now()
		current_time_str = str('{:%I:%M %p}'.format(current_time.time()))

		log_file("{} : Its {} and you are in office with ip address: {}\n".format(date_today, current_time_str, current_ip))
		last_train_in = datetime.datetime.combine(date_today, last_train_time) - datetime.datetime.combine(datetime.date.today(), current_time.time())

		add_minutes = walk_office_to_metro + metro_wait_average + metro_ride_1 + metro_wait_average + metro_ride_2 + walk_metro_to_home
		estimated_arrival = current_time + timedelta(minutes=add_minutes)

		days	= divmod(last_train_in.seconds, 86400)		# Get days
		hours 	= divmod(days[1], 3600)						# Use Reminder of days to calc hours
		minutes	= divmod(hours[1], 60)						# Use Reminder of hours to calc minutes

		time_remaining = "{} hours {} mins".format(hours[0], minutes[0])
		if hours[0] == 0 and minutes[0] < 61:
			webbrowser.open(warning_video)
			notify("Leave now to reach home by {}".format('{:%I:%M %p}'.format(estimated_arrival)), "Last train leaves in {}".format(time_remaining), "ALERT | Last Metro Reminder", 'Hero')
		else:	
			notify("Leave now to reach home by {}".format('{:%I:%M %p}'.format(estimated_arrival)), "Last train leaves in {}".format(time_remaining), "Last Metro Reminder", 'Hero')

	else:
		pass


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