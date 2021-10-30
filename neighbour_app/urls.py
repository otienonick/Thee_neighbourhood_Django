from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import home,my_profile_view,home_page,business_details,post,services

urlpatterns = [
    path('' , home , name = 'home'),
    path('myprofile/',my_profile_view,name ='profile'),
    path('homepage/',home_page,name ='homepage'),
    path('create-post/',post,name ='post'),
    path('services/',services,name ='services'),
    path('business/<str:pk>' , business_details , name='business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)