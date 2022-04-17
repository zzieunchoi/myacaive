comment까지 복습 - django

project 이름 - pjt07

application 이름 - movies/ accounts



## pjt07

```python
# settings.py
INSTALLED_APPS = [
    'movies',
    'accounts',
]
TEMPLATES = [
        'DIRS': [BASE_DIR/ 'templates'],
AUTH_USER_MODEL = 'accounts.User'
```

```python
# pjt07/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
    path('accounts/',include('accounts.urls')),
]
```

```html
<!--pjt07/templates/base.html-->
<body>
  <div class = "mx-5">
  <div class="container">
    {% if request.user.is_authenticated %} <!-- 로그인한 경우-->
      <nav class="navbar fixed-top navbar-light bg-light">
        <div class="container-fluid">
          <h3>♥ Hello, Glad to meet you, {{ user }} ♥</h3>
          <br>
          <div class="d-flex justify-content-end">
          <a class = 'btn btn-warning btn-sm' href="{% url 'accounts:update' %}">Edit profile</a>
          <br>
          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input class = 'btn btn-primary btn-sm' type="submit" value="Logout">
          </form>
          <br>
          <form action="{% url 'accounts:delete' %}" method="POST">
            {% csrf_token %}
            <input class = 'btn btn-danger btn-sm' type="submit" value="Withdrawal">
          </form>
        </div>
          <br> 
        </div>
      </nav>

    {% else %} <!-- 비로그인인 경우-->
    <nav class="navbar sticky-top navbar-light bg-light">
      <div class="container-fluid">
        <h3>★ Before using our site, please LOGIN or SIGNUP ★</h3>
        <br>
        <div class="d-flex justify-content-end">
        <a class = 'btn btn-outline-success btn-sm' href="{% url 'accounts:login' %}">Login</a>
        <br>
        <a class = 'btn btn-outline-danger btn-sm' href="{% url 'accounts:signup' %}">Signup</a>
        </div>
      </div>
    </nav>

    {% endif %}

  </div>
  
  {% block content %}
  
  {% endblock content %}
</div>
</body>
```



## movies

```python
# models.py
from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

```python
# forms.py
from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':'my-title form-control',
                'placeholder':'Enter the title',
                'maxlength': 10,
                }
            ),
        )
    
    description = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder' :'Write description',
            }
        )
    )

    class Meta:
        model = Movie
        exclude= ('user',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'write your comment',
            }
        )
    )
    
    class Meta:
        model = Comment
        fields = ('content',)
```

```python
# urls.py
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

```

```python
# movies/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie
from .models import Comment
from .forms import MovieForm
from .forms import CommentForm

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)  
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'movies/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
    return redirect('movies:index')

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form =MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, movie_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)
```

```html
<!--movies/templates/movies/index.html-->
{% extends 'base.html' %}

{% block content %}
<h1>MOVIE INDEX</h1>
  {% if request.user.is_authenticated %}
    <a class="btn btn-outline-dark btn-sm" href="{% url 'movies:create' %}">NEW MOVIE CREATE</a>
  {% else %}
    <p>If you want to create movie's detail, you should login our site!</p>
  {% endif %}

  <hr>
  
  {% for movie in movies %}
  <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
  <hr>
  {% endfor %}

{% endblock content %}
```

```html
<!--detail.html-->
{% extends 'base.html' %}

{% block content %}
{% if request.user.is_authenticated %}

<h1>DETAIL</h1>
<hr>

<p class="fw-bold">제목 : {{ movie.title }}</p>
<p>{{ movie.description }}</p>
<hr>
<p>If you have better information, please edit our movie's description</p> 
<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:update' movie.pk %}">UPDATE</a>

<form action="{% url 'movies:delete' movie.pk %}" method="POST">
  {% csrf_token %}
  <input class="btn btn-outline-danger btn-sm" type="submit" value="DELETE">
</form>

<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}">back to INDEX</a>
<hr>

<p class="fw-bold">{{ movie.title }}'s review</p>
<ul>
  {% for comment in comments %}
    <li>{{ comment.content }}
      <form action = "{% url 'movies:comments_delete' movie.pk comment.pk %}" method = "POST">
        {% csrf_token %}
          <input class="btn btn-outline-danger btn-sm" type="submit" value = "delete">
      </form>

    </li>
  {% endfor %}
</ul>
<hr>

<form action = "{% url 'movies:comments_create' movie.pk %}" method = "POST">
  {% csrf_token %}
  {{ comment_form }}
  <input class="btn btn-outline-dark btn-sm" type = "submit" value = "submit">
</form>

{% else %}
  <p>If you want to see movie's datail, you should login our site!</p>
  <a class="btn btn-outline-dark btn-sm" href = "{% url 'accounts:login' %}">LOGIN</a>

{% endif %}

{% endblock content %}
```

```html
<!--create.html-->
{% extends 'base.html' %}

{% block content %}

<h1>CREATE</h1>
<h3>Thank you for introducing the movie!</h3>
<hr>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input class="btn btn-outline-dark btn-sm" type="submit">
  </form>
<hr>
<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}">back to INDEX</a>
  
{% endblock content %}
```

```html
<!--update.html -->
{% extends 'base.html' %}

{% block content %}

<h1>UPDATE</h1>

<hr>
<form action="{% url 'movies:update' movie.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <a href="{% url 'movies:update' movie.pk %}">Reset</a>
  <input class="btn btn-outline-dark btn-sm" type="submit" value = "submit">
</form>
<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}">back to INDEX</a>

{% endblock content %}
```



## accounts

```python
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

```python
# forms.py
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

```python
# urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name= 'change_password'),
]
```

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form =CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:update')

    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
```

```html
<!--login.html-->
{% extends 'base.html' %}

{% block content %}
<h1>LOGIN</h1>
<form action="{% url 'accounts:login' %}" method = "POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input class="btn btn-outline-dark btn-sm" type="submit" value = "login">
</form>

{% endblock content %}
```

```html
<!--signup.html-->
{% extends 'base.html' %}

{% block content %}
<h1>WELCOME, signup site</h1>
<hr>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input class="btn btn-outline-dark btn-sm" type="submit">
</form>

{% endblock content %}
```

```html
<!--update.html-->
{% extends 'base.html' %}

{% block content %}
<h1>Modification of member information</h1>
<hr>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input class="btn btn-outline-dark btn-sm" type="submit">
</form>
<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}">NO MODIFICATION</a>
{% endblock content %}
```

```html
<!--change_password.html-->
{% extends 'base.html' %}

{% block content %}
<h1>CHANGE PASSWORD</h1>
<hr>
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input class="btn btn-outline-dark btn-sm" type="submit">
</form>

<a class="btn btn-outline-dark btn-sm" href="{% url 'movies:index' %}">back</a>

{% endblock content %}
```
