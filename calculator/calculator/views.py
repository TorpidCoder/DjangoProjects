from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request,'homepage.html')

def calculate(request):

    Fnumber = request.GET['Fnumber']
    Snumber = request.GET['Snumber']

    addition = int(Fnumber)+int(Snumber)
    subtract = int(Fnumber)-int(Snumber)

    return render(request,'calculate.html' , {'Fnumber':Fnumber , 'Snumber':Snumber , 'addition':addition , 'subtract' : subtract})

def check(request):

    return render(request,'check.html')
