from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    image = CloudinaryField('image')
    identity = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.username}-{self.created}'

    def  save_profile(self):
        self.save()
    


class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    admin = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.admin}'
 

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.save()

    def update_occupants(self):
        self.save()
    
    @classmethod
    def find_neighbourhood(cls,neighbourhood_id = None):
        neighbourhood = cls.objects.filter(id = neighbourhood_id)   
        return neighbourhood   


