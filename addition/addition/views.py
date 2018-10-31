from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request,'homepage.html')


def addition(request):
    fnumber = request.GET['fnumber']
    snumber = request.GET['snumber']
    addition = int(fnumber) + int(snumber)

    return render(request,'calculate.html',{'fnumber':fnumber,'snumber':snumber , 'addition':addition})
