import json


def dec_movies(movies):
    dec_list = []
    for movie in movies:
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8')
        movie_detail_dict = json.load(movie_detail)

        date = movie_detail_dict['release_date']
        if date[5:7] == '12':
            dec_list.append(movie_detail_dict['title'])
    return dec_list
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))