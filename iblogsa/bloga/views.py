from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import Post,Category

# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)



def post(request, url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    return render(request,'posts.html',{'post':post, 'cats':cats})

def category(request, url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})

def about(request):
    return render(request,'about.html')

#superuser id=ajay pass=hixk6946