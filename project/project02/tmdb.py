import requests

class TMDB:
    BASE_URL = 'https://api.themoviedb.org/3'

    def __init__(self, path, title = None):
        self.path = path
        self.params = {
            'api_key': 'e79aae3e1785073280b48567d1478ed2',
            'language':'ko',
            'region': 'KR',
            'query':title,
        }

    def make_data(self):
        data = requests.get(TMDB.BASE_URL + self.path, params = self.params).json()
        return data