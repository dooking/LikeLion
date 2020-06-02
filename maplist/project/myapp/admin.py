from django.contrib import admin

from .models import dolist,Comment
# Register your models here.

admin.site.register(dolist)
admin.site.register(Comment)