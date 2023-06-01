from src.video import Video, PLVideo
from src.channel import Channel

if __name__ == 'main':
    channel = Channel("channel_id")

    video1 = Video('AWX4JnAnjBE')
    video1.title = 'GIL в Python: зачем он нужен и как с этим жить'
    video1.url = 'https://www.youtube.com/watch?v=AWX4JnAnjBE'
    video1.views = 100
    video1.likes = 10

    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    video2.title = 'MoscowPython Meetup 78 - вступление'
    video2.url = 'https://www.youtube.com/watch?v=4fObz_qw9u4'
    video2.views = 200
    video2.likes = 20

    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

    channel.print_info()













# from src.video import Video, PLVideo
# import sys
#
# if __name__ == 'main':
#     # Создаем два экземпляра класса
#     video1 = Video('AWX4JnAnjBE', title='GIL в Python: зачем он нужен и как с этим жить')  # 'AWX4JnAnjBE' - это id видео из ютуб
#     video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', title='MoscowPython Meetup 78 - вступление')
#
#     assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить', f"Ожидалось: GIL в Python: зачем он нужен и как с этим жить, Фактически: {str(video1)}"
#     assert str(video2) == 'MoscowPython Meetup 78 - вступление', f"Ожидалось: MoscowPython Meetup 78 - вступление, Фактически: {str(video2)}"








