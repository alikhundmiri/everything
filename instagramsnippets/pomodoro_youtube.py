import sys, os, webbrowser, random, time
import video_details
video_ids = [
'3-NTv0CdFCk','ybUsle7TzGk',
'TdrL3QxjyVw','eP4eqhWc7sI',
'tCXGJQYZ9JA','rYEDA3JcQqw',
'k1frgt0D_f4','pS-gbqbVd8c']

def pick_video():
	total_videos = len(video_ids)
	video_id = video_ids[random.randint(0,total_videos)]
	return video_id

def notify(title, text, subtitle):
	if subtitle:
		os.system("""
		osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Hero"'
		""".format(title, subtitle, text))
	else:
		os.system("""
		osascript -e 'display notification "{}" with title "{}" sound name "Hero"'
		""".format(title, text))

def play_video(video_id):
	time.sleep(3)
	youtube_url = 'https://www.youtube.com/watch?v={}'.format(video_id)
	webbrowser.open(youtube_url)

if __name__ == '__main__':

	if len(sys.argv[1]) > 1:
		artist_name = sys.argv[1]
	else:
		artist_name = input("Enter the Artist Name: ")

	try:
		input_prompt = sys.argv[1]
		if input_prompt == 'start':
			video_id = pick_video()
			notify("Pomodoro Youtube | By Ali Khundmiri", 'Playing A Song in 3 seconds...', 'Break Time')
			play_video(video_id)
		elif input_prompt == 'stop':
			notify("Pomodoro Youtube | By Ali Khundmiri", 'Times up, Give your 100 percent. All the best.', 'Back to work')

	except IndexError as e:
		print("no platform gives as input")
		video_id = pick_video()
		notify("Pomodoro Youtube | By Ali Khundmiri", 'Playing A Song in 3 seconds...', 'Break Time')
		play_video(video_id)
'''

CRONJOB
25,55 11-15 * * 1-5  /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/everything/instagramsnippets/pomodoro_youtube.py start

30,0 11-15 * * 1-5 /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/everything/instagramsnippets/pomodoro_youtube.py stop
'''