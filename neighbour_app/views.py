from django.shortcuts import render
from . models import  Profile,Post


# Create your views here.

def home(request):
    profile = Profile.objects.get(user = request.user)

    context = {
        'profile':profile,

    }

    return render(request,'neighbour/home.html',context)

def my_profile_view(request):
    profile = Profile.objects.get(user = request.user)

    context = {
        'profile':profile,
    
    }
    return render(request,'profiles/myprofile.html',context)

def home_page(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts,
    }
    return render(request,'neighbour/homepage.html',context)


