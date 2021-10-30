from .models import Profile,Post,Business
from django import forms

# from django.contrib.auth.models import User

class ProfileModelForm(forms.ModelForm):
    identity = forms.CharField(label = 'id')
    

    class Meta:
        model = Profile
        fields = ['username','email','identity','image','hood','location','occupants']



# class NeighbourhoodModelForm(forms.ModelForm):
#     name = forms.CharField(label = 'hood')
    
#     class Meta:
#         model = Neighbourhood
#         fields = ['location','name','occupants']        

class BusinessModelForm(forms.ModelForm):
    name = forms.CharField(label = 'Business name')

    class Meta:
        model = Business
        fields = ['name','image','email','neighbourhood_id']     

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'phone', 'password')