from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import home,my_profile_view

urlpatterns = [
    path('' , home , name = 'home'),
    path('myprofile/',my_profile_view,name ='profile'),





]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)