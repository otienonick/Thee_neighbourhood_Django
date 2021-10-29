from .models import Profile,Post,Neighbourhood
from django import forms

class ProfileModelForm(forms.ModelForm):
    identity = forms.CharField(label = 'id')
    

    class Meta:
        model = Profile
        fields = ['username','email','identity','image']


class NeighbourhoodModelForm(forms.ModelForm):
    name = forms.CharField(label = 'hood')
    

    class Meta:
        model = Neighbourhood
        fields = ['location','name','occupants']        
