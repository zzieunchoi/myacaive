import requests
from pprint import pprint
from tmdb import TMDB

def recommendation(title):
    path = '/search/movie'
    r1 = TMDB(path, title)
    data1 = r1.make_data()
    
    if data1['results']== []:
        return None
    
    movie_id = data1['results'][0]['id']
    # f스트링도 쌉가능 /movie/{movie_id}/recommendations
    path2 = '/movie/'+ str(movie_id) + '/recommendations'
    r2 = TMDB(path2)
    data2 = r2.make_data()
    ans_list = []
    for movie in data2['results']:
        ans_list.append(movie['title'])
    return ans_list


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
