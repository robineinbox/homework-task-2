import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self._api_key = "AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4" # замените на свой API ключ
        self._base_url = "https://www.googleapis.com/youtube/v3"
        self._data = self._get_channel_data()

    def _get_channel_data(self) -> dict:
        """Метод для получения данных о канале по его id"""
        url = f"{self._base_url}/channels?part=snippet&id={self.channel_id}&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_title = self._data["items"][0]["snippet"]["title"]
        channel_description = self._data["items"][0]["snippet"]["description"]
        print(f"Название канала: {channel_title}")
        print(f"Описание канала: {channel_description}")

    def get_playlists(self) -> list:
        """Метод для получения списка плейлистов канала"""
        url = f"{self._base_url}/playlists?part=snippet&channelId={self.channel_id}&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        playlists = []
        for item in data["items"]:
            playlist_id = item["id"]
            playlist_title = item["snippet"]["title"]
            playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
            playlists.append({"id": playlist_id, "title": playlist_title, "url": playlist_url})
        return playlists

    def get_most_popular_video(self) -> str:
        """Метод для получения ссылки на самое популярное видео канала"""
        url = f"{self._base_url}/search?part=snippet&channelId={self.channel_id}&type=video&order=viewCount&maxResults=1&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        video_id = data["items"][0]["id"]["videoId"]
        video_url = f"https://youtu.be/{video_id}"
        return video_url















# from googleapiclient.discovery import build
# import datetime
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         api_key = '<your_api_key_here>'
#         self.youtube = build('youtube', 'v3', developerKey=api_key)
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         request = self.youtube.channels().list(
#             part="snippet,contentDetails,statistics",
#             id=self.channel_id
#         )
#         response = request.execute()
#         items = response['items']
#         channel = items[0]
#         print('Название канала:', channel['snippet']['title'])
#         print('URL-адрес:', f"https://www.youtube.com/channel/{self.channel_id}")
#         print('Описание:', channel['snippet']['description'])
#         print('Количество подписчиков:', channel['statistics']['subscriberCount'])
#         print('Количество просмотров:', channel['statistics']['viewCount'])
#
#
# class PlayList(Channel):
#     """Класс для ютуб-плейлиста"""
#
#     def __init__(self, playlist_id: str):
#         """Экземпляр инициализируется id плейлиста."""
#         super().__init__(playlist_id)
#         self.playlist_id = playlist_id
#         self.title = None
#         self.url = None
#
#         request = self.youtube.playlists().list(part="snippet", id=self.playlist_id)
#         response = request.execute()
#         items = response['items']
#         playlist = items[0]
#         self.title = playlist['snippet']['title']
#         self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
#         self.video_ids = self.get_video_ids()
#
#     def get_video_ids(self):
#         """Метод возвращает список video_id видео в плейлисте"""
#         request = self.youtube.playlistItems().list(
#             part="snippet,contentDetails",
#             playlistId=self.playlist_id,
#             maxResults=50,
#         )
#         response = request.execute()
#         items = response['items']
#         video_ids = [item['contentDetails']['videoId'] for item in items]
#         while 'nextPageToken' in response:
#             request = self.youtube.playlistItems().list(
#                 part="snippet,contentDetails",
#                 playlistId=self.playlist_id,
#                 maxResults=50,
#                 pageToken=response['nextPageToken']
#             )
#             response = request.execute()
#             items = response['items']
#             video_ids.extend([item['contentDetails']['videoId'] for item in items])
#         return video_ids
#
#     @property
#     def total_duration(self):
#         """Метод возвращает объект класса datetime.timedelta со суммарной длительностью плейлиста."""
#         total_duration = 0
#         for video_id in self.video_ids:
#             request = self.youtube.videos().list(
#                 part='contentDetails',
#                 id=video_id
#             )
#             response = request.execute()
#             video = response['items'][0]
#             duration = video['contentDetails']['duration']
#             duration_timedelta = datetime.timedelta(
#                 hours=int(duration[2:].split('H')[0]),
#                 minutes=int(duration[duration.index('H')+1:].split('M')[0]),
#                 seconds=int(duration[duration.index('M')+1:].split('S')[0])
#             )
#             total_duration += duration_timedelta
#         return total_duration
#
#     def show_best_video(self):
#         """Метод возвращает ссылку на самое популярное видео из плейлиста"""
#         video_stats = []
#         for video_id in self.video_ids:
#             request = self.youtube.videos().list(
#                 part='statistics',
#                 id=video_id
#             )
#             response = request.execute()
#
#         video_stats.extend(response['items'])
#         best_video_stats = max(video_stats, key=lambda stats: stats['statistics']['likeCount'])
#         best_video_id = best_video_stats['id']
#         return f"https://youtu.be/{best_video_id}"








# import requests
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.title, self.description = self._get_channel_info()
#
#     def _get_channel_info(self) -> tuple[str, str]:
#         """Возвращает название и описание канала."""
#         base_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={self.channel_id}"
#         response = requests.get(base_url)
#         data = response.json()
#         if 'items' in data and len(data['items']) > 0:
#             title = data['items'][0]['snippet']['title']
#             description = data['items'][0]['snippet']['description']
#             return title, description
#         else:
#             return '', ''
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f"Название канала: {self.title}")
#         print(f"Описание канала: {self.description}")




# from google.auth.transport import requests
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.title, self.url = self._get_channel_info()
#
#     def _get_channel_info(self) -> tuple[str, str]:
#         """Возвращает название и ссылку на канал."""
#         base_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={self.channel_id}"
#         response = requests.get(base_url)
#         data = response.json()
#         title = data['items'][0]['snippet']['title']
#         url = f"https://www.youtube.com/channel/{self.channel_id}"
#         return title, url
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f"Название канала: {self.title}")
#         print(f"Ссылка на канал: {self.url}")




# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.id = channel_id
#         # здесь можно использовать API YouTube для получения названия канала, описания и другой информации
#         self.name = "Moscow Python Meetup"
#         self.description = "Community of Python developers in Moscow"
#         self.url = f"https://www.youtube.com/channel/{channel_id}"
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f"Название канала: {self.name}")
#         print(f"Описание канала: {self.description}")
#         print(f"Ссылка на канал: {self.url}")








































# import json    #Дз_4
# import os
# from googleapiclient.discovery import build
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     api_key: str = os.getenv('YT_API_KEY')
#     youtube = build('youtube', 'v3', developerKey=api_key)
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.title = ''
#         self.description = ''
#         self.url = ''
#         self.subscriber_count = 0
#         self.video_count = 0
#         self.view_count = 0
#
#         # получение соответствующих значений из словаря channel
#         service = self.get_service()
#         channel = service.channels().list(id=channel_id, part='snippet,statistics').execute()
#         if 'items' in channel and len(channel['items']) > 0:
#             snippet = channel['items'][0]['snippet']
#             statistics = channel['items'][0]['statistics']
#             self.title = snippet.get('title', '')
#             self.description = snippet.get('description', '')
#             self.url = 'https://www.youtube.com/channel/' + channel_id
#             self.subscriber_count = int(statistics.get('subscriberCount', 0))
#             self.video_count = int(statistics.get('videoCount', 0))
#             self.view_count = int(statistics.get('viewCount', 0))
#
#     @classmethod
#     def get_service(cls):
#         """Возвращает объект для работы с YouTube API"""
#         return build('youtube', 'v3', developerKey=cls.api_key)
#
#     def to_json(self, filename: str) -> None:
#         """Сохраняет в файл значения атрибутов экземпляра Channel"""
#         data = {
#             'id': self.channel_id,
#             'title': self.title,
#             'description': self.description,
#             'url': self.url,
#             'subscriber_count': self.subscriber_count,
#             'video_count': self.video_count,
#             'view_count': self.view_count
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f'Title: {self.title}')
#         print(f'Description: {self.description}')
#         print(f'URL: {self.url}')
#         print(f'Subscriber count: {self.subscriber_count}')
#         print(f'Video count: {self.video_count}')
#         print(f'View count: {self.view_count}')
#
#
# if __name__ == '__main__':
#     channel_id = 'YOUR_CHANNEL_ID_HERE'
#     channel = Channel(channel_id)
#     channel.print_info()
#     channel.to_json('channel_info.json')
























# import json
# from googleapiclient.discovery import build
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#     API_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.title = ''
#         self.description = ''
#         self.url = ''
#         self.subscriber_count = 0
#         self.video_count = 0
#         self.view_count = 0
#
#         # получение соответствующих значений из словаря channel
#         service = self.get_service()
#         channel = service.channels().list(id=channel_id, part='snippet,statistics').execute()
#         if 'items' in channel and len(channel['items']) > 0:
#             snippet = channel['items'][0]['snippet']
#             statistics = channel['items'][0]['statistics']
#             self.title = snippet.get('title', '')
#             self.description = snippet.get('description', '')
#             self.url = 'https://www.youtube.com/channel/' + channel_id
#             self.subscriber_count = int(statistics.get('subscriberCount', 0))
#             self.video_count = int(statistics.get('videoCount', 0))
#             self.view_count = int(statistics.get('viewCount', 0))
#
#     @classmethod
#     def get_service(cls):
#         """Возвращает объект для работы с YouTube API"""
#         return build('youtube', 'v3', developerKey=cls.API_KEY)
#
#     def to_json(self, filename: str) -> None:
#         """Сохраняет в файл значения атрибутов экземпляра Channel"""
#         data = {
#             'id': self.channel_id,
#             'title': self.title,
#             'description': self.description,
#             'url': self.url,
#             'subscriber_count': self.subscriber_count,
#             'video_count': self.video_count,
#             'view_count': self.view_count
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f'Title: {self.title}')
#         print(f'Description: {self.description}')
#         print(f'URL: {self.url}')
#         print(f'Subscriber count: {self.subscriber_count}')
#         print(f'Video count: {self.video_count}')
#         print(f'View count: {self.view_count}')
#
#
# if __name__ == '__main__':
#     channel_id = 'YOUR_CHANNEL_ID_HERE'
#     channel = Channel(channel_id)
#     channel.print_info()
#     channel.to_json('channel_info.json')

































# class Channel:
#     def __init__(self, channel_id):
#         self.channel_id = channel_id
#
#     def print_info(self):
#         print(f"Channel ID: {self.channel_id}")












































# import json Дз_3
# from googleapiclient.discovery import build
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#     API_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.title = ""
#         self.description = ""
#         self.url = ""
#         self.subscriber_count = 0
#         self.video_count = 0
#         self.view_count = 0
#         self.get_channel_info()
#
#
#     def get_channel_info(self) -> None:
#         """Получает информацию о канале по API и заполняет соответствующие атрибуты"""
#         channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
#         self.title = channel["items"][0]["snippet"]["title"]
#         self.description = channel["items"][0]["snippet"]["description"]
#         self.url = 'https://www.youtube.com/channel/' + self.channel_id
#         self.subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
#         self.video_count = int(channel["items"][0]["statistics"]["videoCount"])
#         self.view_count = int(channel["items"][0]["statistics"]["viewCount"])
#
#     def __str__(self) -> str:
#         """Возвращает название и ссылку на канал в формате <название_канала> (<ссылка_на_канал>)"""
#         return f"{self.title} ({self.url})"
#
#     def __add__(self, other: "Channel") -> int:
#         """Возвращает количество подписчиков двух каналов, если их сложить"""
#         return self.subscriber_count + other.subscriber_count
#
#     def __sub__(self, other: "Channel") -> int:
#         """Возвращает разницу в количестве подписчиков двух каналов"""
#         return self.subscriber_count - other.subscriber_count
#
#     def __gt__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет больше подписчиков, чем второй"""
#         return self.subscriber_count > other.subscriber_count
#
#     def __ge__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет больше или равное количество подписчиков, чем второй"""
#         return self.subscriber_count >= other.subscriber_count
#
#     def __lt__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет меньше подписчиков, чем второй"""
#         return self.subscriber_count < other.subscriber_count
#
#     def __le__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет меньше или равное количество подписчиков, чем второй"""
#         return self.subscriber_count <= other.subscriber_count
#
#     def __eq__(self, other: "Channel") -> bool:
#         """Проверяет, что количество подписчиков двух каналов равно"""
#         return self.subscriber_count == other.subscriber_count
#
#     def to_json(self, filename: str) -> None:
#         """Сохраняет в файл значения атрибутов экземпляра Channel"""
#         data = {
#             'id': self.channel_id,
#             'title': self.title,
#             'description': self.description,
#             'url': self.url,
#             'subscriber_count': self.subscriber_count,
#             'video_count': self.video_count,
#             'view_count': self.view_count
#         }
#         with open(filename, 'w', encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False)
#
#     @classmethod
#     def get_service(cls):
#         """Возвращает объект для работы с YouTube API"""
#         return build('youtube', 'v3', developerKey=cls.API_KEY)
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f'Title: {self.title}')
#         print(f'Description: {self.description}')
#         print(f'URL: {self.url}')
#         print(f'Subscriber count: {self.subscriber_count}')
#         print(f'Video count: {self.video_count}')
#         print(f'View count: {self.view_count}')


























# class Channel:   Дз_3
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#         self.subscribers = 0
#         self.name = ""
#         self.link = ""
#
#     def __str__(self) -> str:
#         """Возвращает название и ссылку на канал в формате <название_канала> (<ссылка_на_канал>)"""
#         return f"{self.name} ({self.link})"
#
#     def __add__(self, other: "Channel") -> int:
#         """Возвращает количество подписчиков двух каналов, если их сложить"""
#         return self.subscribers + other.subscribers
#
#     def __sub__(self, other: "Channel") -> int:
#         """Возвращает разницу в количестве подписчиков двух каналов"""
#         return self.subscribers - other.subscribers
#
#     def __gt__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет больше подписчиков, чем второй"""
#         return self.subscribers > other.subscribers
#
#     def __ge__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет больше или равное количество подписчиков, чем второй"""
#         return self.subscribers >= other.subscribers
#
#     def __lt__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет меньше подписчиков, чем второй"""
#         return self.subscribers < other.subscribers
#
#     def __le__(self, other: "Channel") -> bool:
#         """Проверяет, что первый канал имеет меньше или равное количество подписчиков, чем второй"""
#         return self.subscribers <= other.subscribers
#
#     def __eq__(self, other: "Channel") -> bool:
#         """Проверяет, что количество подписчиков двух каналов равно"""
#         return self.subscribers == other.subscribers
#
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print("Название:", self.name)
#         print("Количество подписчиков:", self.subscribers)
#         print("Ссылка:", self.link)
#
#
#
#
#
#
# import json   Дз_2
# from googleapiclient.discovery import build
#
# class Channel:
#     """Класс для ютуб-канала"""
#     API_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'
#
#     def __init__(self, channel_id: str) -> None:
#     #     """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#     #     self.channel_id = channel_id
#     #     self.title = ''
#     #     self.description = ''
#     #     self.url = ''
#     #     self.subscriber_count = 0
#     #     self.video_count = 0
#     #     self.view_count = 0
#
#         # получение соответствующих значений из словаря channel
#         channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
#         self.title = channel["items"][0]["snippet"]["title"]
#         self.description = channel["items"][0]["snippet"]["description"]
#         self.url = 'https://www.youtube.com/channel/' + channel_id
#         self.subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
#         self.video_count = int(channel["items"][0]["statistics"]["videoCount"])
#         self.view_count = int(channel["items"][0]["statistics"]["viewCount"])
#
#     @classmethod
#     def get_service(cls):
#         """Возвращает объект для работы с YouTube API"""
#         return build('youtube', 'v3', developerKey=cls.API_KEY)
#
#     def to_json(self, filename: str) -> None:
#         """Сохраняет в файл значения атрибутов экземпляра Channel"""
#         data = {
#             'id': self.channel_id,
#             'title': self.title,
#             'description': self.description,
#             'url': self.url,
#             'subscriber_count': self.subscriber_count,
#             'video_count': self.video_count,
#             'view_count': self.view_count
#         }
#         # with open(filename, 'w') as f:
#         #     json.dump(data, f)
#         with open(filename, 'w', encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False)
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         print(f'Title: {self.title}')
#         print(f'Description: {self.description}')
#         print(f'URL: {self.url}')
#         print(f'Subscriber count: {self.subscriber_count}')
#         print(f'Video count: {self.video_count}')
#         print(f'View count: {self.view_count}')
#
#
#
#
#
#
#
# import json   Дз_1
# import os
#
# from googleapiclient.discovery import build
#
#
# api_key: str = os.getenv('YT_API_KEY')
#
#
# youtube = build('youtube', 'v3', developerKey=api_key)
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.channel_id = channel_id
#
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
#         info = json.dumps(channel, indent=2, ensure_ascii=False)
#         print(info)