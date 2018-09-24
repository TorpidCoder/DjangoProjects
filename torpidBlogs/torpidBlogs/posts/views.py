from django.shortcuts import render

from .models import Post




def Homepage(request):

    posts = Post.objects.order_by('pub_date')
    return render(request,'posts/home.html' , {'posts':posts})
