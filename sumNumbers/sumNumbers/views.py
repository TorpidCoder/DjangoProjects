from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request , 'homepage.html')

def sumNumbers(request):

    sum = 0

    number = request.GET['number']

    split_number= [int(val) for val in number]

    for vals in split_number:
        sum+=vals

    return render(request , 'sum.html' , {'number':number , 'sum' : sum})
