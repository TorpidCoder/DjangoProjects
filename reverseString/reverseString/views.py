from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def reverse(request):

    string = request.GET['string']

    reverse = string[::-1]


    return render(request,'reverse.html',{'string':string , 'reverse':reverse})
