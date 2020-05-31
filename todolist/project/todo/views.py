from django.shortcuts import render, redirect
from .models import dolist, Comment
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    dolists = dolist.objects.all().order_by('deadline')
    for do in dolists:
        now = datetime.now().date()
        now2 = do.deadline
        dolist.objects.filter(pk=do.pk).update(
            dday=((now2-now).days)
        )
    return render(request, 'home.html', {'dolists': dolists})

@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        print(request)
        new_post = dolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
            author = request.user
        )
        return redirect('detail', new_post.pk)
        # return render(request,'detail.html',{'new_post':new_post})
    return render(request, 'new.html')


def detail(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)

    if(request.method == "POST"):
        Comment.objects.create(
            post=dolists,
            content=request.POST['content'],
            author = request.user
        )
        return redirect('detail', post_pk)
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


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if(request.method == "POST"):
        found_user = User.objects.get(username=request.POST['username'])
        if(found_user is not None):
            error = 'username이 이미 존재합니다'
            return render(request, 'signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'signup.html')


def login(request):
    if(request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if(found_user is None):
            error='아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'login.html',{'error':error} )
        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend' )
        return redirect(request.GET.get('next','/'))
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')