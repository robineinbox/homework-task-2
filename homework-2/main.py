from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')

import json

if __name__ == '__main__':
    with open('moscowpython.json', 'r') as f:
        data = json.load(f)

    moscowpython = Channel(data['id'])
    moscowpython.title = data['title']
    moscowpython.description = data['description']
    moscowpython.url = data['url']
    moscowpython.subscriber_count = data['subscriber_count']
    moscowpython.video_count = data['video_count']
    moscowpython.view_count = data['view_count']

    # выводим значения атрибутов из объекта moscowpython
    print(moscowpython.title)
    print(moscowpython.video_count)
    print(moscowpython.url)