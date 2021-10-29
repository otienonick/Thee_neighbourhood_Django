from django.shortcuts import render,redirect
from . models import  Profile,Post,Neighbourhood
from .forms  import ProfileModelForm,NeighbourhoodModelForm


# Create your views here.

def home(request):
    profile = Profile.objects.get(user = request.user)

    context = {
        'profile':profile,

    }

    return render(request,'neighbour/home.html',context)

def my_profile_view(request):
 
    profile = Profile.objects.get(user = request.user)
    neighbour = Neighbourhood.objects.get(admin = request.user)
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)

    context = {
        'profile':profile,
        'form':form,
        'neighbour':neighbour,
    
    }

    return render(request,'profiles/myprofile.html',context)


def update_location(request):
    neighbour = Neighbourhood.objects.get(admin = request.user)
    n_form = NeighbourhoodModelForm(request.POST or None ,instance = neighbour)
    if n_form.is_valid():
            neighbour.save()
            return redirect('profile')
    context = {
        'n_form':n_form
    }

    return render(request,'profiles/update_location.html',context)

def home_page(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts,
    }
    return render(request,'neighbour/homepage.html',context)


