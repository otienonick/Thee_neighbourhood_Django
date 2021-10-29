from django.shortcuts import render,redirect
from . models import  Profile,Post,Neighbourhood,Business
from .forms  import ProfileModelForm,NeighbourhoodModelForm,BusinessModelForm


# Create your views here.

def home(request):
    profile = Profile.objects.get(user = request.user)
    biz = Business.objects.all()

    context = {
        'profile':profile,
        'biz':biz,


    }

    return render(request,'neighbour/home.html',context)

def my_profile_view(request):
    biz = Business.objects.all()
    profile = Profile.objects.get(user = request.user)
    neighbour = Neighbourhood.objects.get(admin = request.user)
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)

    context = {
        'profile':profile,
        'form':form,
        'neighbour':neighbour,
        'biz':biz,

    
    }

    return render(request,'profiles/myprofile.html',context)


def update_location(request):
    neighbour = Neighbourhood.objects.get(admin = request.user)
    biz = Business.objects.all()

    n_form = NeighbourhoodModelForm(request.POST or None ,instance = neighbour)
    if n_form.is_valid():
            neighbour.save()
            return redirect('profile')
    context = {
        'n_form':n_form,
        'biz':biz,


    }

    return render(request,'profiles/update_location.html',context)

def home_page(request):
    posts = Post.objects.all().order_by('-created')
    biz = Business.objects.all()

    
    context = {
        'posts':posts,
        'biz':biz,

    }
    return render(request,'neighbour/homepage.html',context)

def business_details(request,pk):
    post = Business.objects.get(pk = pk)
    b_form = BusinessModelForm(request.POST or None,request.FILES or None)

    if b_form.is_valid():
            instance = b_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('homepage')
    b_form = BusinessModelForm()            

    context = {

        'business':post,
        'b_form':b_form,

    }
    return render(request,'neighbour/business.html',context)




