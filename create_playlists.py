
import json
import requests
from secrets import spotify_client_id, spotify_secret

class Playlists:
    def __init__(self):
        self.client_id = spotify_client_id

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
new_playlist.create_playlist()
