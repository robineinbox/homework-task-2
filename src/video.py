class Video:
    def __init__(self, video_id):
        self.youtube = None
        self.video_id = video_id
        self.title = ""
        self.url = ""
        self.views = 0
        self.likes = 0

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
         return super().__str__()
