from django.contrib import admin

from .models import Post,Comment,UserInfo,Survey,CardNews
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserInfo)
admin.site.register(Survey)
admin.site.register(CardNews)