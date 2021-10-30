from django.shortcuts import render,redirect
from . models import  Profile,Post,Business
from .forms  import ProfileModelForm,BusinessModelForm,PostModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    biz = Business.objects.all()

    context = {
        'biz':biz,

    }

    return render(request,'neighbour/home.html',context)

def my_profile_view(request):
    biz = Business.objects.all()
    profile = Profile.objects.get(user = request.user)
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)

    context = {
        'profile':profile,
        'form':form,
        'biz':biz,

    }

    return render(request,'profiles/myprofile.html',context)


@login_required(login_url='/accounts/login/')
def home_page(request):
    posts = Post.objects.all().order_by('-created')
    biz = Business.objects.all()

    
    context = {
        'posts':posts,
        'biz':biz,

    }
    return render(request,'neighbour/homepage.html',context)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def post(request):
    posts = Post.objects.all().order_by('-created')
    p_form = PostModelForm(request.POST or None,request.FILES or None)

    if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    p_form = PostModelForm()    

    context = {

        'p_form':p_form,
        'posts':posts

    }
    return render(request,'neighbour/post.html',context)

