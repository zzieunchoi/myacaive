import requests
from pprint import pprint
from tmdb import TMDB

def credits(title):
    path1 = '/search/movie'
    r1 = TMDB(path1, title)
    data1 = r1.make_data()
    
    if data1['results']== []:
        return None

    movie_id = data1['results'][0]['id']
    path2 = '/movie/' + str(movie_id) +'/credits'
    r2 = TMDB(path2)
    data2 = r2.make_data()
    
    actor_list = [] 
    for movie in data2['cast']: 
        if movie['cast_id'] < 10: 
            actor_list.append(movie['name']) 

    director_list = [] 
    for movie in data2['crew']: 
        if movie['department'] == 'Directing': 
            director_list.append(movie['name']) 

    ans_dict = dict()
    ans_dict['cast'] = actor_list
    ans_dict['crew'] = director_list

    return ans_dict

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
