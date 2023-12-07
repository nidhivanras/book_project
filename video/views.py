from django.shortcuts import render
from googleapiclient.discovery import build


# Create your views here.
def videos_list(request):
    api_key = 'AIzaSyCJQ2WoCt9gMmdKlkaRS_NqEyNeNyxDm9k'
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the latest videos from a specific channel (replace 'CHANNEL_ID' with your channel ID)
    channel_id = 'UCH-cK1RIBzsbVlNnWDD0nHw'
    response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',
        type='video',
        maxResults=10  # You can adjust the number of videos to retrieve
    ).execute()

    videos = response.get('items', [])
    return render(request, 'videos_list.html', {'videos': videos})
