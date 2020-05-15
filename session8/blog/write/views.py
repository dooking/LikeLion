from django.shortcuts import render, redirect
from .models import article


# Create your views here.

def index_defined_in_view(request):
    articles = article.objects.all()
    new_article = []
    for row in articles:
        if(len(row.title)>5):
            new_article.append(row)
    return render(request, 'index.html', {'articles': new_article})

def detail_defined_in_view(request, num_title):
    contents = article.objects.get(pk=num_title)
    return render(request, 'detail.html', {'contents': contents.content})

def new_defined_in_view(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
        )
        return redirect('detail', num_title=new_article.pk)
    else:
        return render(request, 'new.html')
