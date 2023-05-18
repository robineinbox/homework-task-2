class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        pass

    def to_json(self, filename: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass








# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         pass
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         pass
































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



