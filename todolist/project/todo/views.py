from django.shortcuts import render, redirect
from .models import dolist, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from project.settings import KAKAO_JS_KEY
from project.settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_STORAGE_BUCKET_NAME,AWS_S3_REGION_NAME
# Create your views here.
import boto3
from boto3.session import Session
from datetime import datetime
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
        file_to_upload = request.FILES.get('img')
        new_post = dolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
            author = request.user,
            img = img_upload(request,file_to_upload)
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
            author = request.user,
        )
        return redirect('detail', post_pk)
    return render(request, 'detail.html', {'dolist': dolists})


def delete(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)
    dolists.delete()
    return redirect('home')


def edit(request, post_pk):
    dolists = dolist.objects.get(pk=post_pk)
    if request.method == "POST":
        file_to_upload = request.FILES.get('img')
        dolist.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
            img = img_upload(request,file_to_upload)
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'dolists': dolists})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if(request.method == "POST"):
        found_user = User.objects.filter(username=request.POST['username'])
        if(found_user is None):
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

def map(request):
    return render(request,'map.html',{'KAKAO_JS_KEY':KAKAO_JS_KEY})

def img_upload(request, file_to_upload):
    session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
    s3 = session.resource('s3')
    now = datetime.now().strftime("%Y%H%M%S")
    user_pk = str(request.user.pk)+'/'

    img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key =  now + user_pk + file_to_upload.name,
        Body = file_to_upload
    )
    s3_url = 'https://dooking-file-upload.s3.ap-northeast-2.amazonaws.com/' + now + user_pk + file_to_upload.name
    return s3_url
    
