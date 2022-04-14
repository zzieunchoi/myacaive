import json
from pprint import pprint


def movie_info(movie, genres):
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    # 새로운 dict 만들어주기
    ans_dict = dict()
    
    # keys 에 들어있는 key를 가져올건데
    for key in keys:
        value = movie.get(key)
        # key가 genre_ids 라면 genre_names로 변환
        if key == 'genre_ids':
            genre_names = []
            # movie.json의 id와 genres.json의 id가 같다면 그걸 append
            for dict_d in genres:
                for i in range(len(movie['genre_ids'])):
                    if dict_d['id'] == movie['genre_ids'][i]:
                        genre_names.append(dict_d['name'])
                ans_dict['genre_names']=genre_names
        # key가 genre_ids가 아니라면 그대로~
        else:
            ans_dict[key] = value
    return ans_dict



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
