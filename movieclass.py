import videos

class Movie(videos.Video):

    """Class used to describe Movies, a child of the class 'Video'"""
    
    def __init__(self, name, video_type, story, poster_url, youtube_url):
        videos.Video.__init__(self, name, video_type)

        # The newer attributes
        self.storyline = story
        self.trailer = youtube_url
        self.poster = poster_url

