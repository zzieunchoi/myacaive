import json

def max_revenue(movies):
    movie_revenue_title = ''
    movie_revenue = 0
    # movies_list의 id를 모두 돌려봐 그 id와 동일한 파일 이름의 json 파일에 들어가서
    for movie in movies:
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8')
        movie_detail_dict = json.load(movie_detail)
    # 그 json 파일의 revenue를 revenue_list에 append 시키고
        
        if movie_detail_dict['revenue'] > movie_revenue:
            movie_revenue = movie_detail_dict['revenue']
            movie_revenue_title = movie_detail_dict['title']
    
    return movie_revenue_title
    
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))