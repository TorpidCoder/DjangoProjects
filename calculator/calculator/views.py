from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request,'homepage.html')

def addition(request):

    Fnumber = request.GET['Fnumber']
    Snumber = request.GET['Snumber']

    addition = int(Fnumber)+int(Snumber)

    return render(request,'calculate.html' , {'Fnumber':Fnumber , 'Snumber':Snumber , 'addition':addition})

def subtract(request):

    Fnumber = request.GET['Fnumber']
    Snumber = request.GET['Snumber']

    subtract = int(Fnumber)-int(Snumber)

    return render(request,'calculate.html' , {'Fnumber':Fnumber , 'Snumber':Snumber ,'subtract' : subtract})
