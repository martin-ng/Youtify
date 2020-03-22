import json
import requests

from secrets import spotify_client_id, spotify_secret

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


class Playlists():
    def __init__(self):
        self.client_id = spotify_client_id
        self.youtube_client = self.get_youtube_client
        print(self.youtube_client)
        print(self.client_id)

    def get_youtube_client(self):

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        # Download from Youtube Oauth
        client_secrets_file = "CLIENT_SECRETS.json"

        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)


        credentials = flow.run_console()

        # Youtube Web API Docs
        youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
        return youtube

    def get_youtube_liked_videos(self):
        request = self.youtube_client.videos().list(part="snippet,contentDetails,statistics", myRating="like")
        response = request.execute()

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Videos",
            "description": "Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.client_id)

        response = requests.post(
            query,
            data=request_body,
        )

        response_json = response.json()
        print("response json: ", response_json)

        # print("query: ", query)


# Testing functions

new_playlist = Playlists()

# new_playlist.create_playlist()
# new_playlist.get_youtube_client()
# new_playlist.get_youtube_liked_videos()
