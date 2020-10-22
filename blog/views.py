from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
def index(request):
   prod = Blogpost.objects.all( )
   params ={"prod":prod}
   return render(request, 'blog/index.html' ,params)
def blogpost(request,post_id):
    post = Blogpost.objects.filter( post_id = post_id)[0]




    return render(request, 'blog/blogpost.html',{"post":post})