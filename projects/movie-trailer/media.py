import json
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def __repr__(self):
        return json.dumps(self.__dict__)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def load_from_json(self, json):
        self.title = json['title']
        self.storyline = json['storyline']
        self.poster_image_url = json['poster_image_url']
        self.trailer_youtube_url = json['trailer_youtube_url']
