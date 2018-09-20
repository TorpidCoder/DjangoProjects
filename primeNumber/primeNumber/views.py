from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')

def isPrime(request):

    isPrime = True

    number = request.GET['number']
    for vals in range(2,10):
        if(int(number)%vals==0):
            isPrime = False

    if(isPrime):
        check = "Is prime"
    else:
        check = "Is not Prime"

    return render(request, 'result.html',{'number':number,str('check'):check})
