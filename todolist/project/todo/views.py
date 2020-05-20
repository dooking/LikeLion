from django.shortcuts import render,redirect
from .models import dolist
from datetime import datetime
# Create your views here.


def home(request):
    dolists = dolist.objects.all().order_by('deadline')
    for do in dolists:
        now = datetime.now().date()
        now2 = do.deadline
        dolist.objects.filter(pk=do.pk).update(
            dday = ((now2-now).days)
        )
    return render(request, 'home.html', {'dolists': dolists})


def new(request):
    if request.method == "POST":
        print(request)
        new_post = dolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
        )
        return redirect('detail', new_post.pk)
        # return render(request,'detail.html',{'new_post':new_post})
    return render(request, 'new.html')


def detail(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'dolist': dolists})


def delete(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)
    dolists.delete()
    return redirect('home')


def edit(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)
    if(request.method == "POST"):
        dolist.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'dolists': dolists})
