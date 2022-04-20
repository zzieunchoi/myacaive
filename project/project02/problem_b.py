import requests
from pprint import pprint
from tmdb import TMDB

def vote_average_movies():
    path = '/movie/popular'
    r = TMDB(path)
    data = r.make_data()
    list = []
    # for i in range(len(data.get('results'))):
    for movie in data.get('results'):
        if movie['vote_average']>=8:
            list.append(movie['title'])
    return list

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
