from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length = 255,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    image = CloudinaryField('image')
    identity = models.IntegerField(null=True ,default='12345678')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    hood = models.CharField(max_length=255,default='mtaa yako')
    location = models.CharField(max_length=255,default='areacode')
    occupants = models.IntegerField(null=True,blank=True,default='5000')


    def __str__(self):
        return f'{self.username}-{self.created}'

    def  save_profile(self):
        self.save()

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

    

class Business(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = CloudinaryField('image')
    neighbourhood_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}-{self.neighbourhood_id}'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.save()
    
    @classmethod
    def find_business(cls,business_id = None):
        business = cls.objects.filter(id = business_id)   
        return business       

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = CloudinaryField('image')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return str(self.title[:30])

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.save()

    @classmethod
    def find_post(cls,post_id = None):
        post = cls.objects.filter(id = post_id)   
        return post       


    class Meta:
        ordering = ['-created'] 

        



    

