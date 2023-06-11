from googleapiclient.discovery import build
from datetime import timedelta
import isodate


class PlayList:
    def __init__(self, playlist_id, api_key):
        self.playlist_id = playlist_id
        self.api_key = "AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4"
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.playlist_info = self.youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def get_playlist_videos(self):
        playlist_items = self.youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id,
            maxResults=50
        ).execute()
        playlist_video_ids = [video['contentDetails']['videoId'] for video in playlist_items['items']]
        video_response = self.youtube.videos().list(
            part='contentDetails, statistics',
            id=','.join(playlist_video_ids)
        ).execute()
        return video_response

    @property
    def total_duration(self):
        video_response = self.get_playlist_videos()
        duration = timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        best_video = \
        sorted(self.get_playlist_videos()['items'], key=lambda x: int(x['statistics']['likeCount']), reverse=True)[0]
        video_id = best_video['id']
        return f"https://youtu.be/{video_id}"




























# from googleapiclient.discovery import build
# from datetime import timedelta
#
# class PlayList:
#     def __init__(self, playlist_id, api_key):
#         self.youtube = build('youtube', 'v3', developerKey=api_key)
#         self.playlist_id = playlist_id
#         self.api_key = api_key
#         playlist_info = self.youtube.playlists().list(
#             part='snippet',
#             id=self.playlist_id).execute()
#         self.title = playlist_info['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
#         self.playlist_url = self.url
#
#     @property
#     def total_duration(self):
#         video_info = self.youtube.playlistItems().list(
#             part='contentDetails',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         total_time = timedelta()
#         for vid in video_info['items']:
#             duration = vid['contentDetails'].get('duration', 'PT0S')
#             time_obj = duration_converter(duration)
#             total_time += time_obj
#         return total_time
#
#     def show_best_video(self):
#         video_info = self.youtube.playlistItems().list(
#             part='snippet',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         best_video = sorted(video_info['items'], key=lambda x: int(x['snippet']['likeCount']), reverse=True)[0]
#         video_id = best_video['snippet']['resourceId']['videoId']
#         return f"https://youtu.be/{video_id}"
#
#
#
# def duration_converter(duration):
#     time = timedelta()
#     time_dict = {
#         'H': 3600,
#         'M': 60,
#         'S': 1,
#     }
#     time_list = duration.replace('PT', '').replace('H', ':').replace('M', ':').replace('S', '').split(':')
#     if len(time_list)==1 and time_list[0]=='':
#         time_list[0]='0:0'
#     for t in time_list:
#         if not t:
#             continue
#         t_time = ''
#         for i in range(len(t)):
#             if t[i].isalpha():
#                  t_time += f"{time_dict[t[i]] * int(t[i - 1]):02}"
#         time += timedelta(seconds=int(t_time))
#     return time












# from googleapiclient.discovery import build
# from datetime import timedelta
#
# class PlayList:
#     def __init__(self, playlist_id, api_key):
#         self.youtube = build('youtube', 'v3', developerKey=api_key)
#         self.playlist_id = playlist_id
#         self.api_key = api_key
#         playlist_info = self.youtube.playlists().list(
#             part='snippet',
#             id=self.playlist_id).execute()
#         self.title = playlist_info['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
#         self.playlist_url = self.url
#
#     @property
#     def total_duration(self):
#         video_info = self.youtube.playlistItems().list(
#             part='contentDetails',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         total_time = timedelta()
#         for vid in video_info['items']:
#             duration = vid['contentDetails'].get('duration', 'PT0S')
#             time_obj = duration_converter(duration)
#             total_time += time_obj
#         return total_time
#
#     def show_best_video(self):
#         video_info = self.youtube.playlistItems().list(
#             part='snippet',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         best_video = sorted(video_info['items'], key=lambda x: int(x['snippet']['likeCount']), reverse=True)[0]
#         video_id = best_video['snippet']['resourceId']['videoId']
#         return f"https://youtu.be/{video_id}"




# def duration_converter(duration):
#     time = timedelta()
#     time_dict = {
#         'H': 3600,
#         'M': 60,
#         'S': 1,
#     }
#     time_list = duration.replace('PT', '').split('M')
#     if len(time_list) == 2:
#         time_list[0] = '0H' + time_list[0]
#     for t in time_list:
#         if not t:
#             continue
#         t_time = ''
#         for i in range(len(t)):
#             if t[i].isalpha():
#                 t_time += f"{time_dict[t[i]] * int(t[i - 1]):02}"
#         time += timedelta(seconds=int(t_time))
#     return time
def duration_converter(duration):
    time = timedelta()

    time_dict = {
        'H': 3600,
        'M': 60,
        'S': 1,
    }

    time_unit = ''
    time_value = ''
    for i in range(len(duration)):
        if duration[i].isdigit():
            time_value += duration[i]
        elif duration[i].isalpha():
            time_unit += duration[i]

            if time_unit in time_dict:
                time += timedelta(seconds=int(time_value) * time_dict[time_unit])

                time_value = ''
                time_unit = ''

    return time
















# from googleapiclient.discovery import build
# from datetime import timedelta
#
# class PlayList:
#     def __init__(self, playlist_id, api_key):
#         self.youtube = None
#         self.playlist_id = playlist_id
#         self.api_key = "AIzaSyCpRKc2CHbfcdMypAQV007jeeq9jufpQHo"
#
#         youtube = build('youtube', 'v3', developerKey=self.api_key)
#         playlist_info = youtube.playlists().list(
#             part='snippet',
#             id=self.playlist_id
#         ).execute()
#
#         self.title = playlist_info['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
#         self.playlist_url = self.url
#
#     @property
#     def total_duration(self):
#         video_info = self.youtube.playlistItems().list(
#             part='contentDetails',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         total_time = timedelta()
#         for vid in video_info['items']:
#             duration = vid['contentDetails'].get('duration', 'PT0S')
#             time_obj = duration_converter(duration)
#             total_time += time_obj
#         return total_time
#
#     def show_best_video(self):
#         video_info = self.youtube.playlistItems().list(
#             part='snippet',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         best_video = sorted(video_info['items'], key=lambda x: int(x['snippet']['likeCount']), reverse=True)[0]
#         video_id = best_video['snippet']['resourceId']['videoId']
#         return f"https://youtu.be/{video_id}"
#
# def duration_converter(duration):
#     time = timedelta()
#     time_dict = {
#         'H': 3600,
#         'M': 60,
#         'S': 1,
#     }
#     time_list = duration.replace('PT', '').split('M')
#     if len(time_list) == 2:
#         time_list[0] = '0H' + time_list[0]
#     for t in time_list:
#         if not t:
#             continue
#         t_time = ''
#         for i in range(len(t)):
#             if t[i].isalpha():
#                 t_time += f"{time_dict[t[i]] * int(t[i - 1]):02}"
#         time += timedelta(seconds=int(t_time))
#     return time

















# from googleapiclient.discovery import build
# from datetime import timedelta
#
#
# class PlayList:
#     def __init__(self, playlist_id):
#         self.youtube = build('youtube', 'v3', developerKey="AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4")
#         playlist_info = self.youtube.playlists().list(
#             part='snippet',
#             id=playlist_id
#         ).execute()
#         self.title = playlist_info['items'][0]['snippet']['title']
#         self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
#         self.playlist_id = playlist_id
#
#     @property
#     def total_duration(self):
#         video_info = self.youtube.playlistItems().list(
#             part='contentDetails',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         total_time = timedelta()
#         for vid in video_info['items']:
#             duration = vid['contentDetails']['duration']
#             time_obj = duration_converter(duration)
#             total_time += time_obj
#         return total_time
#
#     def show_best_video(self):
#         video_info = self.youtube.playlistItems().list(
#             part='snippet',
#             playlistId=self.playlist_id,
#             maxResults=50
#         ).execute()
#         best_video = sorted(video_info['items'], key=lambda x: int(x['snippet']['likeCount']), reverse=True)[0]
#         video_id = best_video['snippet']['resourceId']['videoId']
#         return f"https://youtu.be/{video_id}"
#
#
# def duration_converter(duration):
#     time = timedelta()
#     time_dict = {
#         'H': 3600,
#         'M': 60,
#         'S': 1,
#     }
#     time_list = duration.replace('PT', '').split('M')
#     if len(time_list) == 2:
#         time_list[0] = '0H' + time_list[0]
#     for t in time_list:
#         if not t:
#             continue
#         t_time = ''
#         for i in range(len(t)):
#             if t[i].isalpha():
#                 t_time += f"{time_dict[t[i]] * int(t[i - 1]):02}"
#         time += timedelta(seconds=int(t_time))
#     return time







# from src.video import PLVideo
# import datetime
# from googleapiclient.discovery import build
#
#
# class PlayList:
#     def __init__(self, playlist_id):
#         self.playlist_id = playlist_id
#         self.videos = []
#         self.youtube = build('youtube', 'v3', developerKey='your_developer_key_here')
#         self.get_videos_from_playlist()
#
#     def get_videos_from_playlist(self):
#         response = self.youtube.playlistItems().list(part='snippet', playlistId=self.playlist_id,
#                                                      maxResults=50).execute()
#         while response:
#             for item in response['items']:
#                 video_id = item['snippet']['resourceId']['videoId']
#                 self.videos.append(PLVideo(video_id, self.playlist_id))
#             if 'nextPageToken' in response:
#                 response = self.youtube.playlistItems().list(part='snippet', playlistId=self.playlist_id, maxResults=50,
#                                                              pageToken=response['nextPageToken']).execute()
#             else:
#                 break
#         self.calculate_total_duration()
#
#     def calculate_total_duration(self):
#         total_seconds = sum(map(lambda video: int(video.duration.total_seconds()), self.videos))
#         self.total_duration = datetime.timedelta(seconds=total_seconds)
#
#     def show_best_video(self):
#         most_views = -1
#         best_video = None
#         for video in self.videos:
#             if int(video.views) > most_views:
#                 most_views = int(video.views)
#                 best_video = video
#         return best_video.url


















# import requests
# import datetime
# from collections import defaultdict
#
#
# class PlayList:
#
#     def __init__(self, playlist_id):
#         self.playlist_id = playlist_id
#         self.title, self.url, self.videos = self._get_playlist_metadata()
#
#     def _get_playlist_metadata(self):
#         playlist_api_url = "https://www.googleapis.com/youtube/v3/playlists"
#         playlist_response = requests.get(
#             playlist_api_url,
#             params={
#                 "key": "AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4",
#                 "part": "snippet",
#                 "id": self.playlist_id,
#             }
#         ).json()
#
#         playlist_snippet = playlist_response['items'][0]['snippet']
#         playlist_title = playlist_snippet['title']
#         playlist_url = "https://www.youtube.com/playlist?list=" + self.playlist_id
#
#         videos_api_url = "https://www.googleapis.com/youtube/v3/playlistItems"
#         video_response = requests.get(
#             videos_api_url,
#             params={
#                 "key": "AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4",
#                 "part": "snippet,contentDetails,statistics",
#                 "playlistId": self.playlist_id,
#                 "maxResults": 50,
#             }
#         ).json()
#
#         videos_list = defaultdict(list)
#         for item in video_response['items']:
#             snippet = item['snippet']
#             content = item['contentDetails']
#             stats = item['statistics']
#
#             video_id = content['videoId']
#             title = snippet['title']
#             url = "https://youtu.be/" + video_id
#             views = int(stats['viewCount'])
#             likes = int(stats['likeCount'])
#             dislikes = int(stats['dislikeCount'])
#             duration = datetime.datetime.strptime(content['duration'], "PT%MM%SS")
#             videos_list[video_id] = [title, url, duration, views, likes, dislikes]
#
#         return playlist_title, playlist_url, videos_list
#
#     @property
#     def total_duration(self):
#         duration = sum([video[2] for video in self.videos.values()], datetime.timedelta())
#         return duration
#
#     def show_best_video(self):
#         _, video_url, _, _, likes, _ = max(self.videos.values(), key=lambda x: x[4])
#         return video_url




















# import requests
# import datetime
#
# class PlayList:
#     """Класс для плейлиста на ютуб-канале"""
#
#     def __init__(self, playlist_id: str) -> None:
#         """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""
#         self.playlist_id = playlist_id
#         self.title, self.url = self._get_playlist_info()
#
#     def _get_playlist_info(self) -> tuple[str, str]:
#         """Возвращает название и ссылку на плейлист."""
#         base_url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={self.playlist_id}"
#         response = requests.get(base_url)
#         data = response.json()
#         title = data['items'][0]['snippet']['title']
#         url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
#         return title, url
#
#     @property
#     def total_duration(self) -> datetime.timedelta:
#         """Возвращает общую продолжительность плейлиста."""
#         base_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={self.playlist_id}"
#         total_duration = datetime.timedelta()
#         while True:
#             response = requests.get(base_url)
#             data = response.json()
#             for item in data['items']:
#                 duration_str = item['contentDetails']['duration']
#                 duration = datetime.datetime.strptime(duration_str, "PT%MM%SS")
#                 total_duration += datetime.timedelta(minutes=duration.minute, seconds=duration.second)
#             if "nextPageToken" in data:
#                 base_url = f"{base_url}&pageToken={data['nextPageToken']}"
#             else:
#                 break
#         return total_duration
#
#     def show_best_video(self) -> str:
#         """Возвращает ссылку на видео с наибольшим количеством лайков."""
#         base_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={self.playlist_id}"
#         best_video_url = ""
#         best_video_likes = 0
#         while True:
#             response = requests.get(base_url)
#             data = response.json()
#             for item in data['items']:
#                 video_likes = item['snippet']['thumbnails']['default']['url']
#                 video_url = f"https://youtu.be/{item['snippet']['resourceId']['videoId']}"
#                 if video_likes > best_video_likes:
#                     best_video_likes = video_likes
#                     best_video_url = video_url
#             if "nextPageToken" in data:
#                 base_url = f"{base_url}&pageToken={data['nextPageToken']}"
#             else:
#                 break
#         return best_video_url
