from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html',context)


def new(request):

    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #두번쨰 방법
    article = Article(title = title, content = content)
    article.save()
    
    #세번째 방법
    # Article.objects.create(title= title, content= content)
    return render(request, 'articles/create.html')