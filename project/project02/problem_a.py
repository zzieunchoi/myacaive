import requests
from tmdb import TMDB

def popular_count():
    path= '/movie/popular'
    r = TMDB(path)
    data = r.make_data()
    ans = len(data.get('results'))
    return ans

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
