from django.test import TestCase
from .models import Profile,Business,Post
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create()
        self.oti = Profile(username = 'test_username',user = user, email = 'test_email',identity = '123456',created = '28-10-2021',updated = '28-10-2021' ,hood = 'test_hood',location = 'test_location',occupants = '5000')

    def test_instance(self):
        self.assertTrue(isinstance(self.oti,Profile))    

    def test_save_method(self):
        self.oti.create_neighbourhood()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)   

    def tearDown(self):
        Profile.objects.all().delete()

    def test_delete_method(self):
        self.oti.create_neighbourhood()
        self.oti.delete_neighbourhood()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)     

    def test_update_method(self):
        self.oti.update_neighbourhood()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0) 

    def test_update_occupants__method(self):
        self.oti.update_occupants()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)    

    def test_find_neighbourhood(self):
        neighbourhood_id = Profile.find_neighbourhood()
        self.assertTrue(len(neighbourhood_id) == 0)    
  

class BusinessTestClass(TestCase):

    def setUp(self):
        user = User.objects.create()
        self.oti = Profile(username = 'test_username',user = user, email = 'test_email',identity = '123456',created = '28-10-2021',updated = '28-10-2021' ,hood = 'test_hood',location = 'test_location',occupants = '5000')
        self.oti.save()

        self.new_business = Business(name = 'test_business_name',user = user,neighbourhood_id = self.oti,email = 'test_email',phone_number = '0718849600')
        self.new_business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business)) 


    def tearDown(self):
            Profile.objects.all().delete()
            Business.objects.all().delete()

    def test_delete_method(self):
            self.new_business.create_business()
            self.new_business.delete_business()
            business = Business.objects.all()
            self.assertTrue(len(business) == 0)  

    def test_update_method(self):
            self.new_business.update_business()
            business = Business.objects.all()
            self.assertTrue(len(business) > 0)     

    def test_find_business(self):
        business_id = Business.find_business()
        self.assertTrue(len(business_id) == 0)         


class PhotoTestClass(TestCase):
        def setUp(self):
            user = User.objects.create()
            self.new_post = Post(title ='test_name',content = 'test_content',created = '2021-10-23',author = user )
            

        def test_instance(self):
            self.assertTrue(isinstance(self.new_post,Post))   

        def test_save_method(self):
            self.new_post.create_post()
            post = Post.objects.all()
            self.assertTrue(len(post) > 0)    

        def tearDown(self):
            Post.objects.all().delete()
            Profile.objects.all().delete()

        def test_delete_method(self):
            self.new_post.create_post()
            self.new_post.delete_post()
            post = Post.objects.all()
            self.assertTrue(len(post) == 0)    

        def test_update_method(self):
            self.new_post.create_post()
            self.new_post.update_post()
            post = Post.objects.all()
            self.assertTrue(len(post) > 0) 


        def test_find_post(self):
            post_id = Post.find_post()
            self.assertTrue(len(post_id) == 0)         



     










    
    







