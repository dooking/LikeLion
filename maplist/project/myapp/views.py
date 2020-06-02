from django.shortcuts import render, redirect
from .models import dolist, Comment
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from project.settings import KAKAO_JS_KEY

def map(request):
    return render(request,'map.html',{'KAKAO_JS_KEY':KAKAO_JS_KEY})