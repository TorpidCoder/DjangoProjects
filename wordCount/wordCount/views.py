from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')

def wordcount(request):

    sum = 0

    sentence = request.GET['sentence']

    for vals in sentence.split(' '):

        sum+=1


    return render(request,'wordcount.html' , {'sentence':sentence , 'sum':sum })
