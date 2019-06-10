'''
RUN THIS SCRIPT TO GET YOUR YOUTUBE CHANNEL DETAILS.

For reference view this: https://developers.google.com/youtube/v3/docs/
'''


import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

youtube_API_KEY = os.environ.get('youtube_API_KEY')
youtube_client_id = os.environ.get('youtube_client_id')
youtube_client_secret = os.environ.get('youtube_client_secret')

# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_all_my_playlist():
	# Disable OAuthlib's HTTPS verification when running locally.
	# *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

	api_service_name = "youtube"
	api_version = "v3"
	client_secrets_file = "client_secret_439209974922-m59fld3bd2hflnkt8e0g2ke7jdqlilq7.apps.googleusercontent.com.json"

	# Get credentials and create an API client
	flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
		client_secrets_file, scopes)
	credentials = flow.run_console()
	youtube = googleapiclient.discovery.build(
		api_service_name, api_version, credentials=credentials)

	request = youtube.playlists().list(
		part="snippet,contentDetails",
		maxResults=25,
		mine=True
	)
	response = request.execute()

	print(response)

def main():
	# Disable OAuthlib's HTTPS verification when running locally.
	# *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

	api_service_name = "youtube"
	api_version = "v3"
	client_secrets_file = "client_secret_439209974922-m59fld3bd2hflnkt8e0g2ke7jdqlilq7.apps.googleusercontent.com.json"

	# Get credentials and create an API client
	flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
		client_secrets_file, scopes)
	credentials = flow.run_console()
	youtube = googleapiclient.discovery.build(
		api_service_name, api_version, credentials=credentials)

	request = youtube.channels().list(
		part="snippet,contentDetails,statistics",
		mine=True
	)
	response = request.execute()

	print(response)

if __name__ == "__main__":
	# main()
	get_all_my_playlist()