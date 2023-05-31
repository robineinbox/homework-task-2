class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        print(f"Channel ID: {self.channel_id}")












































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