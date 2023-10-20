from googleapiclient.discovery import build
import json

youtubeApi = 'your youtube-api'
playlist = 'PLoNrs8WVbJDT_q9GZOxHPsYqLN2kYWjI8'
nextPage_token = None

youtube = build('youtube', 'v3', developerKey=youtubeApi)

playlist_videos = []

while True:
    res = youtube.playlistItems().list(part='snippet', playlistId=playlist, maxResults=20).execute()
    playlist_videos += res['items']

    nextPage_token = res.get('nestPageToken')

    if nextPage_token is None:
        break


playlist_videos = res['items']

json_formatted_str = json.dumps(playlist_videos, indent=2)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_formatted_str, f, ensure_ascii=False, indent=4)


