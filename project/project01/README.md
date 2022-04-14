# project 1

python을 활용한 데이터 수집 1



* 목표

```
1. Python 기본 문법 실습
2. 파일 입출력에 대한 이해
3. 데이터 구조에 대한 분석과 이해
4. 데이터를 가공하고 JSON 형태로 저장 
```



* 요구 사항

```
커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출해 나가
는 과정을 진행합니다. 
```



movie.json 가져오기

genres.json

```json
[
  {
    "id": 28,
    "name": "Action"
  },
  {
    "id": 12,
    "name": "Adventure"
  },
  {
    "id": 16,
    "name": "Animation"
  },
  {
    "id": 35,
    "name": "Comedy"
  },
  {
    "id": 80,
    "name": "Crime"
  },
  {
    "id": 99,
    "name": "Documentary"
  },
  {
    "id": 18,
    "name": "Drama"
  },
  {
    "id": 10751,
    "name": "Family"
  },
  {
    "id": 14,
    "name": "Fantasy"
  },
  {
    "id": 36,
    "name": "History"
  },
  {
    "id": 27,
    "name": "Horror"
  },
  {
    "id": 10402,
    "name": "Music"
  },
  {
    "id": 9648,
    "name": "Mystery"
  },
  {
    "id": 10749,
    "name": "Romance"
  },
  {
    "id": 878,
    "name": "Science Fiction"
  },
  {
    "id": 10770,
    "name": "TV Movie"
  },
  {
    "id": 53,
    "name": "Thriller"
  },
  {
    "id": 10752,
    "name": "War"
  },
  {
    "id": 37,
    "name": "Western"
  }
]
```

movie.json

```json
{
    "adult": false,
    "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
    "genre_ids": [
        18,
        80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
    "popularity": 67.931,
    "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
    "release_date": "1995-01-28",
    "title": "쇼생크 탈출",
    "video": false,
    "vote_average": 8.7,
    "vote_count": 18040
}
```

movies.json

```json
[
  {
    "adult": false,
    "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
    "genre_ids": [
      18,
      80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
    "popularity": 67.931,
    "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
    "release_date": "1995-01-28",
    "title": "쇼생크 탈출",
    "video": false,
    "vote_average": 8.7,
    "vote_count": 18040
  },
  {
    "adult": false,
    "backdrop_path": "/rSPw7tgCH9c6NqICZef4kZjFOQ5.jpg",
    "genre_ids": [
      18,
      80
    ],
    "id": 238,
    "original_language": "en",
    "original_title": "The Godfather",
    "overview": "시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.",
    "popularity": 65.193,
    "poster_path": "/cOwVs8eYA4G9ZQs7hIRSoiZr46Q.jpg",
    "release_date": "1972-12-27",
    "title": "대부",
    "video": false,
    "vote_average": 8.7,
    "vote_count": 13622
  },
 ...
]
```







A. 제공되는 영화 데이터의 주요내용 수집

movie.json 파일 활용하여  id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보 가져옴

가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성

```
딕셔너리 이용하기
a = {'도건':'부산', '송윤':'울산', '지은':'수원', '승현':'창원'}

value 값 가져오기
1. 바로 인덱스 가져오기
print(a['송윤']) 
# '울산'
2. .get 가져오기 (에러가 나타나면 반환하는 값을 지정 가능함-None)
print(a.get('도건'))
# '부산'
```



```python
import json
from pprint import pprint


def movie_info(movie):
    ans_dict = dict()
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids'
]
    for key in keys:
        ans_dict[key] = movie.get(key)  
    return ans_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



B. 제공되는 영화 데이터의 주요내용 수정 

데이터에서 id, title, poster_path, vote_average, overview, genre_ids키에 해당하는 정보만 가져오는데, genre_ids 대신 그에 맞는 genre_names로 변환하여 dictionary를 반환하는 movie_info 가져오기

```python
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
```



C. 다중 데이터 분석 및 수정

movies라는 20개의 영화데이터가 주어진다. 서비스 구성에 필요한 정보만 뽑아 반환하는 movie_info 함수를 완성. B와 동일한 구조, 단 리스트로 뽑아내기 위해 모든 dict를 list에 넣어줌

```python
import json
from pprint import pprint


def movie_info(movies, genres):
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    # 새로운 dict 만들어주기
    ans_list = list()
    
    # keys 에 들어있는 key를 가져올건데
    for movie in movies:
        ans_dict = dict()
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
        ans_list.append(ans_dict)
    return ans_list

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```



D. 알고리즘을 통한 데이터 출력 

세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성. movies 폴더 내에는 각 movie의 id를 제목으로 하는 .json 파일이 들어가있음

수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성

```python
import json


def max_revenue(movies):
    # 초기값 지정
    movie_revenue_title = ''
    movie_revenue = 0
    # movies_list의 id를 모두 돌려봐 그 id와 동일한 파일 이름의 json 파일에 들어가서
    for movie in movies:
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8')
        movie_detail_dict = json.load(movie_detail)
        
        # 계속 제일 큰걸로 할당
        if movie_detail_dict['revenue'] > movie_revenue:
            movie_revenue = movie_detail_dict['revenue']
            movie_revenue_title = movie_detail_dict['title']
    
    return movie_revenue_title
    
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```



E. 알고리즘을 통한 데이터 출력 

세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉 한 영화들의 제목 리스트를 출력하는 알고리즘을 작성. 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies를 완성

```python
import json


def dec_movies(movies):
    dec_list = []
    for movie in movies:
        # 그 movie에 해당하는 id를 이용해 그 id가 제목인 .json파일을 불러옴
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8')
        movie_detail_dict = json.load(movie_detail)
        # date를 가져와서 2022-04-13형식으로 되어있으니 5~6번째 글자가 12면 list에 추가
        date = movie_detail_dict['release_date']
        if date[5:7] == '12':
            dec_list.append(movie_detail_dict['title'])
    return dec_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```

