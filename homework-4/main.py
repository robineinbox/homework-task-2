from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

    video_response = video1.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video1.video_id).execute()
    video1.title = video_response['items'][0]['snippet']['title']
    print(video1.title)

    playlist_response = video2.youtube.playlists().list(part='snippet', id=video2.playlist_id).execute()
    video2.title = playlist_response['items'][0]['snippet']['title']
    print(video2.title)












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
