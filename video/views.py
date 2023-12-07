from django.shortcuts import render
from googleapiclient.discovery import build


# Create your views here.
from lookup.models import LookupField


def videos_list(request):
    video_length = LookupField.objects.filter(code='video_length')
    if video_length:
        video_length = video_length[0].desc
    else:
        video_length = 9
    api_key = 'AIzaSyCJQ2WoCt9gMmdKlkaRS_NqEyNeNyxDm9k'
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the latest videos from a specific channel (replace 'CHANNEL_ID' with your channel ID)
    channel_id = 'UCH-cK1RIBzsbVlNnWDD0nHw'
    response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',
        type='video',
        maxResults=video_length  # You can adjust the number of videos to retrieve
    ).execute()

    videos = response.get('items', [])
    return render(request, 'videos_list.html', {'videos': videos})
