from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted')

def insert_WebPage(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter urls')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse ('Webpage is inserted')

def insert_AccessRecord(request):
    n=input('enter name')
    WO=WebPage.objects.get_or_create(name=n)[0]
    WO.save()
    a=input('enter author')
    d=input('enter value')
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AO.save()
    return HttpResponse ('accessrecord is inserted')
