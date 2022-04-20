# project 02

python을 활용한 데이터 수집 2

* 목표

```
1. Python 기초 문법 실습
2. 데이터 구조에 대한 분석과 이해
3. 요청과 응답에 대한 이해
4. API의 활용과 문서 분석 
```



* 요구사항

```
커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 영화 데이터를 수집하는 과정
```



TMDB API(https://developers.themoviedb.org/3)에서 데이터 가져오기

[tmdb movie database](https://developers.themoviedb.org/3/getting-started/authentication)

A. 인기 영화 조회

인기 영화의 개수를 출력, requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냄, popular를 기준으로 받아온 데이터에서 영화 리스트의 개수를 계산하고 계산한 정보를 반환하는 함수 popular_count를 완성합니다.





B. 특정 조건에 맞는 인기 영화 조회 I 

받아온 데이터에서 vote_average를 기준으로 점수가 8 이상인 영화들의 목록을 리스트로 반환하는 함수 vote_average_movies를 완성





C. 특정 조건에 맞는 인기 영화 조회 II 

받아온 데이터 중 평점이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수 ranking을 완성

```python
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
```



이 때 필요한거!

sorted 다시 공부하기

```
Key를 기준으로 정렬 (오름차순)

my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
sorted_dict = sorted(my_dict.items())
print(sorted_dict)
#[('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 1)]

참고로, my_dict.items()를 출력해보면 다음과 같이 Tuple pair로 이루어진 List가 리턴됩니다.
print(my_dict.items())
# dict_items([('c', 3), ('a', 1), ('b', 2), ('e', 1), ('d', 2)])

Key를 기준으로 정렬 (내림차순)
내림차순으로 정렬하려면 sorted()에 다음과 같이 reverse = True를 인자로 전달해야 합니다. 여기서 lambda가 인자로 전달되는데 item[0]는 dict의 key를 의미합니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
print(sorted_dict)
# [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 1)]

Value를 기준으로 정렬 (오름차순)
다음과 같이 sorted()를 사용하여 Value를 기준으로 정렬할 수 있습니다. 인자로 lambda가 전달되는데 item[1]은 dict의 Value를 의미합니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
print(sorted_dict)
# [('a', 1), ('e', 1), ('b', 2), ('d', 2), ('c', 3)]

Value를 기준으로 정렬 (내림차순)
내림차순으로 정렬하려면 다음과 같이 sorted()에 인자로 reverse = True를 전달하면 됩니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
print(sorted_dict)
# [('c', 3), ('b', 2), ('d', 2), ('a', 1), ('e', 1)]
```





D. 특정 영화 추천 영화 조회 

requests를 이용하여 영화 검색(Search Movies) 요청을 보내고 응답 받은 결과를 바탕으로 id를 찾아 추천영화 목록 조회 (Get Recommendations) URL을 생성.

결과:

```
TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장
저장된 리스트를 반환하는 함수 recommendation을 완성
올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환
id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환
```





E. 배우, 감독 리스트 출력 

영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력합니다. 

requests를 이용하여 영화 검색(Search Movies) 요청을 보냄. 응답 받은 결과를 바탕으로 id를 찾아 크레딧 조회 (Get Credits) URL을 생성. requests를 이용하여 URL에 요청을 보냄

결과:

```
cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장
department 값이 Directing인 감독의 이름을 리스트에 저장
반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우리스트와
감독리스트를 value로 갖음
완성된 딕셔너리를 반환하는 함수 credits을 완성
```



F. 특정 영화 배우, 감독 리스트 조회

영화 데이터를 제공하는 다른 API를 사용하여 요청을 보내고 추가적인 정보를 수집하는 함수를 완성

```
다른 API
1. KMDB(https://www.kmdb.or.kr/info/api/apiDetail/6)
2. 영진위(https://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)
3. 네이버 영화검색 API(https://developers.naver.com/docs/search/movie/)
```

