# REST-API

## HTTP

hyper text transfer protocol

웹상에서 컨텐츠를 전송하기 위한 약속

HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜

웹에서 이루어지는 모든 데이터 교환의 기초

```
요청: 클라이언트에 의해 전송되는 메시지
응답: 서버에서 응답으로 전송되는 메시지
```



기본 특징

* Stateless
* connectionless

쿠키와 세션을 통해 서번 상태를 요청과 연결하도록 함

![image-20220420090559679](220420_RESTAPI.assets/image-20220420090559679.png)



http request methods

자원에 대한 행위를 정의, 주어진 리소스에 수행하길 원하는 행동을 나타냄

GET(조회), POST(작성), PUT(수정), DELETE(삭제)



HTTP response status codes

```
1xx informational responses
2xx successful responses
3xx redirection responses
4xx client error responses
5xx server error responses
```



웹에서의 리소스 식별

HTTP 요청의 대상을 리소스라고 함

리소스는 문서, 사진 또는 어떤 것이든 될 수 있음

각 리소스는 리소스 식별을 위해 http 전체에서 사용되는 uri로 식별된



URL, URN

* URL
  * 통합자원 위치
  * 네트워크 상에 자원이 어디있는지 알려주기 위한 약속
  * 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
  * 웹주고, 링크라고도 불림
* URN
  * 통합자원이름
  * URL로 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함
  * 예시) ISBN

* URI
  * 통합자원 식별자
  * 인터넷의 자원을 식별하는 유일한 주소(정보의 자원을 표현)
  * 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
  * 하위개념: URL, URN
  * URI는 URN과 URL로 나눌 수 있지만, URN을 사용하는 비중이 매우 작기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함

URI의 구조(https://www.example.com:80/path/to/myfile.html/?key=value#quick-start)

* scheme(protocol)
  * 브라우저가 사용해야 하는 프로토콜
  * http(s), data, file, ftp, mailto
  * htts://
* Host(Domain name)
  * 요청을 받은 웹 서버의 이름
  * IP address를 직접 사용할수도 있지만, 실 사용시 불편하므로 웹에서 그리 자주 사용되지는 않음
  * www.example.com
* port
  * 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문
  * http 프로토콜의 표준 포트
    * http 80
    * https 443
  * :80
* path
  * 웹 서버 상의 리소스 경로
  * 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 물리적인 실제 위치가 아닌 추상화 형태의 구조로 표현
  * /path/to/myfile.html
* Query
  * query string parameters
  * 웹 서버에 제공되는 추가적은 매개 변수
  * &로 구분되는 key-value 목록
  * ?key=value
* fragment
  * anchor
  * 자원 안에서의 북마크의 한 종류를 나타냄
  * 브라우저에서 해당 문서의 특정 부분을 보여주기 위한 방법
  * 브라우저에게 알려주는 요소이기 떄문에 fragment identifier 라고 부르며 # 뒤의 부분은 요청이 서버에 보내지지 않음
  * #quick-start



## RESTful API

RESTful services, simply REST services라고도 부름

프로그래밍을 통해 클라이언트의 요청에 json을 응답하는 서버를 구성

지금까지 사용자의 입장에서 썼던 API를 제곡자의 입장이 되어 개발해보기

* API
  * application programming interface
  * 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터 페이스
    * 애플리케이션과 프로그램으로 소통하는 방법
    * CLI는 명령줄, GUI는 그래픽, API는 프로그래밍을 통해 특정한 기능 수행
  * WEB API
    * 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
    * 여러 OPEN API사용
  * 응답 데이터 타입
    * HTML, XML, JSON등
  * YOUTUBE API, Kakao Map API 등,,,



* REST
  * REpresentational State Transfer
  * API server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  * 네트워크 구조 원리의 모음
    * 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
  * REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭함
  * 자원을 정의하는 방법에 대한 고민
    * 정의된 자원을 어디에 위치 시킬 것인가
  * REST의 자원과 주소의 지정 방법
    * 자원: URI
    * 행위: HTTP METHOD
    * 표현
      * 자원과 행위를 통해 궁극적으로 표현되는 결과물
      * JSON으로 표현된 데이터를 제공
  * 핵심 규칙
    * 정보는 URI로 표현
    * 자원에 대한 행위는 HTTP method로 표현(GET, POST, PUT, DELETE)
    * 설계방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지는 않지만 설계 방법론은 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음

* JSON
  * JSON is a lightweight data - interchange format
  * javascript의 표기법을 따른 단순 문자열
  * 특징
    * 사람이 읽거나 쓰기 쉽고 기계가 파싱하고 만들어내기 쉬움
    * 파이썬의 dictionary, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료 구조로 쉽게 변화할 수 있는 key-value 형태의 구조를 갖고 있음



## Response

가상환경 설정

```bash
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

```python
# settings.py
INSTALLED APPS = [
    'articles',
    'django_seed' ]
```

```python
# my_api/urls.py
urlpatterns = [
    path('api/v1/', include('articles:urls')),
]
```

```python
# articles/urls.py
urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
]
```

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
```

```bash
$ python manage.py seef articles --number=20
```

```python
# urls.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
# 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어줄 필요없음
```

```html
<!--article.html-->
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
```



api/v1/html

![image-20220420101152883](220420_RESTAPI.assets/image-20220420101152883.png)



api/v1/json-1

![image-20220420101307249](220420_RESTAPI.assets/image-20220420101307249.png)



```
* content-type(개발자 도구에서 확인)
데이터의 media type을 나타내기 위해 사용됨
응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

* JsonResponse objects
json-encoded response를 만드는 HTTPresponser의 서브 클래스
'safe' parametrer(기본값: true)
 - dict 이외의 객체를 직렬화하려면 false로 설정해야함
```



serialization(직렬화)
: 데이터 베이스로부터 사용자에게 json으로 줘야된느데 바로 변환이 불가능하다. 다른 데이터 타입으로 용이하게 바꿔주기 위한 과정. 

데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정



serializers in django
queryset 및 model instance와 같은 복잡한 데이터를 json, xml 등의 유형으로 쉽게 변환할 수 있는 **python 데이터 타입**으로 만들어줌



DRF(Django REST framework) 라이브러리

[rest framework](https://www.django-rest-framework.org/)

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',
]
```

```python
# serializers.py
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

게시글에 대한 정보 쿼리셋을 serialize 하는 도구

```python
# views.py

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    # default: many = False(단일객체)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

![image-20220420103517877](220420_RESTAPI.assets/image-20220420103517877.png)



```python
$ pip install requests
import requests
reponse = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
pprint(response.json())
# 우리가 직접 만들어본걸로 data 가져오기!
```



DRF

![image-20220420110216238](220420_RESTAPI.assets/image-20220420110216238.png)



## Single Model

DRF with single model

단일 모델의 data를 직렬화하여 json으로 변환하는 방법에 대한 학습

단일 모델을 두고 CRUD 로직을 수행가능하도록 설계

API 개발을 위한 핵심 기능을 제공하는 도구 활용

​	DRF built-in form

​	Postman

* API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
* 설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성 할 수 있도록 도움



```python
INSTALLED_APPS = [
    'articles',
    'django_seed',
    'django_extensions',
    'rest_framework',
```

```python
# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```

```python
# urls.py
from django.urls import path
from . import views


urlpatterns = [

]
```

```python
#models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



model serializer

모델 필드에 해당하는 필드가 있는 serializer클래스를 자동으로 만들 수 있는 shorcut

모델정보에 맞춰 자동으로 필드생성, serializer에 대한 유효성 검사기를 자동으로 생성, .create() & .update()의 간단한 기본 구현이 포함됨

model필드를 어떻게 직렬화 할지 설정하는 것이 핵심

이 과정을 django에서 model의 필드를 설정하는 것과 동일함

```python
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```



```bash
pip install ipython
python manage.py shell_plus
from articles.serializers import ArticleListSerializer
serializer = ArticleListSerializer()
serializer
article = Article.objects.get(pk=1)
serializer = ArticleListSerializer(article)
serializer.data
articles = Article.objects.all() # 단일객체가 아님
serializer = ArticleListSerializer(articles, many = True)
serializer.data()
```





## 1:N relation

