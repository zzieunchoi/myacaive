from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # 역순으로 보는 방법
    #articles = Article.objects.all()[::-1]
    #articles = Article.objects.order_by('-pk')

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
    return redirect('articles:index')

def detail_01(request, pk):
    articles = Article.objects.get(pk=pk)
    # 역순으로 보는 방법
    #articles = Article.objects.all()[::-1]
    #articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/detail.html',context)


def detail_02(request, title):
    articles = Article.objects.filter(title = title)
    # 역순으로 보는 방법
    #articles = Article.objects.all()[::-1]
    #articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/detail.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.title)