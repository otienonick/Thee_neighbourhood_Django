from .models import Profile,Post
from django import forms

class ProfileModelForm(forms.ModelForm):
    identity = forms.CharField(label = 'id')
    

    class Meta:
        model = Profile
        fields = ['username','email','identity','image']
