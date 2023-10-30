from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Date = models.DateField()

    def new_comment(self, data):
        comment = Comment()
        comment.Author = data['name']
        comment.Email = data['email']
        comment.Message = data['message']
        comment.Article = self
        comment.Date = datetime.now().date()
        comment.save()


class Comment(models.Model):
    Author = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Date = models.DateField()