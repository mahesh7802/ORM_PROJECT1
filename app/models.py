from django.db import models
from app.models import *
# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,primary_key=True)
    url=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    author=models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self) -> str:
        return self.author


