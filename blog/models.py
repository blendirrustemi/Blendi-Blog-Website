from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    profile_pic = models.ImageField(default="blendi_rrustemi.png" , null=True, blank=True)
    rep_link = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
    