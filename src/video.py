import requests

class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.title = None
        self.description = None
        self.like_count = None
        self.view_count = None
        self.comment_count = None

        try:
            data = requests.get(
                f'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={self.video_id}&key=YOUR_API_KEY').json()
            self.title = data['items'][0]['snippet']['title']
            self.description = data['items'][0]['snippet']['description']
            self.like_count = data['items'][0]['statistics']['likeCount']
            self.view_count = data['items'][0]['statistics']['viewCount']
            self.comment_count = data['items'][0]['statistics']['commentCount']
        except:
            self.title = None
            self.description = None
            self.like_count = None
            self.view_count = None
            self.comment_count = None

# from src.video import Video
#
# if __name__ == '__main__':
#     broken_video = Video('broken_video_id')
#     assert broken_video.title is None
#     assert broken_video.description is None
#     assert broken_video.like_count is None
#     assert broken_video.view_count is None
#     assert broken_video.comment_count is None
































# from googleapiclient.discovery import build   #Дз_5
#
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'
# DEVELOPER_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'
#
#
# class Video:
#
#     def __init__(self, video_id):
#         self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
#         self.video_id = video_id
#
#         video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
#         self.title = video_response['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/watch?v={self.video_id}"
#         self.views = video_response['items'][0]['statistics']['viewCount']
#
#     def __str__(self):
#         return self.title
#
#
# class PLVideo(Video):
#
#     def __init__(self, video_id, playlist_id):
#         super().__init__(video_id)
#         self.playlist_id = playlist_id
#
#     def __str__(self):
#         return super().__str__()





#
# from googleapiclient.discovery import build   #Дз_4
#
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'
# DEVELOPER_KEY = 'API_KEY'
#
#
# class Video:
#     def __init__(self, video_id):
#         self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#                              developerKey=DEVELOPER_KEY)
#         self.video_id = video_id
#         video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
#         self.title = video_response['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/watch?v={self.video_id}"
#         self.views = video_response['items'][0]['statistics']['viewCount']
#         self.likes = video_response['items'][0]['statistics']['likeCount']
#
#     def __str__(self):
#         return self.title
#
#
# class PLVideo(Video):
#     def __init__(self, video_id, playlist_id):
#         super().__init__(video_id)
#         self.playlist_id = playlist_id
#
#     def __str__(self):
#          return super().__str__()