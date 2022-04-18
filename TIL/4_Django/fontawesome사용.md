# fontawesome 사용하는 방법

먼저 head에 fontawesome 키 가져와서 title 위에 넣기!

1. button 대신 아이콘 집어넣기

```html
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-white">
      {% if request.user not in article.like_users.all %}
        <i class="far fa-heart"></i>
      {% else %}
        <i class="fas fa-heart" style="color: red;"></i>
      {% endif %}
    </button>
  </form>
  <p>{{ article.like_users.count }}명이 좋아합니다.</p>

```



2. input에 아이콘 넣기

```html
<input type ="submit" class = "search" value = "아이콘_해당_유니코드_입력;"></input>
```

