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
    phone_number = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': 'format...0718849600'}))


    class Meta:
        model = Business
        fields = ['name','image','email','neighbourhood_id','phone_number']     

class NewsLetterForm(forms.Form):
    email = forms.EmailField(label='Email')