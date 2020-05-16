from django.db import models

# Create your models here.
class Article(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    time = models.TimeField()
    
    def __str__(self):
        return self.title