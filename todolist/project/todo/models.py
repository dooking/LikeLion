from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class dolist(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField()
    dday = models.IntegerField(default = 0)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(dolist, on_delete=models.CASCADE, related_name = 'comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'ccomments' )