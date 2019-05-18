import os, webbrowser, random, time
import video_details
video_ids = [
'3-NTv0CdFCk',
'TdrL3QxjyVw',
'eP4eqhWc7sI',
'tCXGJQYZ9JA',
'rYEDA3JcQqw',
'k1frgt0D_f4',
'pS-gbqbVd8c']

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
	youtube_url = 'https://www.youtube.com/watch?v={}'.format(video_id)
	webbrowser.open(youtube_url)

if __name__ == '__main__':
	video_id = pick_video()
	video_details.video_details(video_id)
	notify("Pomodoro Youtube | By Ali Khundmiri", 'Playing A Song in 3 seconds...', 'Break Time')
	time.sleep(3)
	play_video(video_id)