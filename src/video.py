import os

from googleapiclient.discovery import build


class Video:
    YT_APY_KEY = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_APY_KEY)

    def __init__(self, id_video):
        self.id = id_video
        video = self.youtube.videos().list(part="snippet,statistics,contentDetails,topicDetails",
                                           id=f'{self.id}').execute()
        try:
            self.title = video['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/video/{self.id}'
            self.view_count = video['items'][0]['statistics']['viewCount']
            self.like_count = video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, id_video, id_play_list):
        super().__init__(id_video)
        self.id_play_list = id_play_list
