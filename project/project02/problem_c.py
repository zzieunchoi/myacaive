import requests
from pprint import pprint
from tmdb import TMDB

def ranking():
    path = '/movie/popular'
    r = TMDB(path)
    data = r.make_data()

    movie_dict = dict()
    for movie in data.get('results'):
        movie_dict[movie['title']]= movie['vote_average']

    sorted_dict = sorted(movie_dict.items(), key = lambda item: item[1], reverse =True)
    print(sorted_dict)
    ans_list = []
    for i in range(5):
        ans_list.append(sorted_dict[i][0])

    return ans_list

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
