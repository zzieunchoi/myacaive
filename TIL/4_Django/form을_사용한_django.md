# model

```python
# models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
```



# form

```python
from django import forms
from .models import Article 

# model form 말고 단순 form
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget = forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs = {
                'class': '제목',
                'placeholder': 'Enter the title',
            }
        ),
    )

    # model에 있는거 가져오기 위해서는 modelform!
    class Meta:
        model = Article
        # 다 가져와!
        fields = '__all__'
        # fields = ['title', 'content']
```



** modelform과 form 의 차이

```
1. form
 - 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너    리를 생성
 - cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야함
 - model에 연관되지 않은 데이터를 받을 때 사용
 
2. modelform
 - django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
 - 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save()호출 가능
```



** 위젯 라벨링 하기

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs = {
                'class':'my-title form-control',
                'placeholder':'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs = {
                'class':'my-content form-control',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages = {
            'required': 'please enter your content'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
```





# urls

1. project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



2. applications/urls.py

```python
from django.urls import path 
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```



# views

```python
# applications/views.py
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성검사
        if form.is_valid():
            # 유효하면 저장
            # instance=article이 없다면 새 인스턴스를 생성하는 것
            article = form.save()
            return redirect('articles:detail', article.pk)
    # post method가 아닌 경우 form은 받아오지마~
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# modelform 말고 그냥 form 사용할 경우
# 유효성 검사 밑에
# title = form.cleaned_data.get('title')
# content = form.cleaned_data.get('content')
# article = Article.objects.create(title=title, content=content)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # instance = article이 있어야 update
        # 없으면 create
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 여기서 instance가 필요!
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:datail', article.pk)
```



# templates

1. project/templates/base.html

```html
<body>
  <div class="container mx-5 my-5">
  {% block content %}
  
  {% endblock %}
</div>
</body>

```



2. applications/templates/applications/

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
  <h2>Articles</h2>
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
  {% endfor %}
{% endblock %}
```



```html
<!-- create.html -->
{% extends 'base.html' %}

{% block content %}
  <h2>CREATE</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="CREATE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```



```
as_p(): 각 필드가 단락으로 감싸져서 렌더링
as_ul(): 각 필드가 목록 항목(li태그)로 감싸져서 렌더링
as_table(): 각 필드가 테이블(tr태그)행으로 감싸져서 렌더링
```





```html
<!-- detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h2>Detail</h2>
  <h2>{{ article.title }}</h3>
  <p>{{ article.content }}</p>
  <p>작성일: {{ article.created_at }}</p>
  <p>수정일: {{ article.updated_at }}</p>
  

  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <br>
  <form action="{% url 'articles:delete' article.pk %}" method = "POST">
    {% csrf_token %}
    <input type = "submit" value = "Delete">
  </form>
  <br>
  <a href="{% url 'articles:index' %}">BACK</a>
  {% endblock %}
```



```html
<!-- update.html -->
{% extends 'base.html' %}

{% block content %}
<h1> UPDATE</h1>

  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE">
  </form>
  <hr>
  <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock %}
```

