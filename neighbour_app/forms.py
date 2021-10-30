from .models import Profile,Post,Business
from django import forms

# from django.contrib.auth.models import User

class ProfileModelForm(forms.ModelForm):
    identity = forms.CharField(label = 'id')
    

    class Meta:
        model = Profile
        fields = ['username','email','identity','image','hood','location','occupants']



class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3} ))
    location = forms.CharField(label = 'Your hood')

    class Meta:
        model = Post
        fields = ['title','content','image']



  



class BusinessModelForm(forms.ModelForm):
    name = forms.CharField(label = 'Business name')

    class Meta:
        model = Business
        fields = ['name','image','email','neighbourhood_id']     

