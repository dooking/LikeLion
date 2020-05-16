from django.shortcuts import render,redirect
from .models import Article
import datetime
# Create your views here.
def view_count():
    count_list = []
    count_list.append(Article.objects.filter(category = "movie").count())
    count_list.append(Article.objects.filter(category = "drama").count())
    count_list.append(Article.objects.filter(category = "entertain").count())
    return count_list

def view_index(request):
    count_list = view_count()
    return render(request, 'index.html',{'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]}) 
 
def view_detail(request,pk_article):
    articles = Article.objects.get(pk=pk_article)
    count_list = view_count()
    return render(request, 'detail.html',{'articles':articles,'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]})

def view_new(request):
    count_list = view_count()
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            category=request.POST['category'],
            title=request.POST['title'],
            content=request.POST['content'],
            time = datetime.datetime.now()
        )
        return redirect('detail', pk_article=new_article.pk)
    else:
        return render(request, 'new.html',{'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]})

def view_movie(request):
    articles = Article.objects.all()
    new_article = []
    count_list = view_count()
    for article in articles:
        if(article.category == "movie"):
            new_article.append(article)
    return render(request,'movie.html',{'articles':new_article,'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]})

def view_drama(request):
    articles = Article.objects.all()
    new_article = []
    count_list = view_count()
    for article in articles:
        if(article.category == "drama"):
            new_article.append(article)
    return render(request,'drama.html',{'articles':new_article,'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]})

def view_entertain(request):
    articles = Article.objects.all()
    new_article = []
    count_list = view_count()
    for article in articles:
        if(article.category == "entertain"):
            new_article.append(article)
    return render(request,'entertain.html',{'articles':new_article,'movie_cnt':count_list[0],'drama_cnt':count_list[1],'entertain_cnt':count_list[2]})