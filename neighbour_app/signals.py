from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save , sender = User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
# def post_save_create_neighbourhood(sender,instance,created,**kwargs):
#     if created:
#         Neighbourhood.objects.create(user = instance)        