from cloudinary.api import usage
from django.test import TestCase
from .models import Profile,Neighbourhood
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create()
        self.oti = Profile(username = user, email = 'test_email',identity = '123456',created = '28-10-2021',updated = '28-10-2021' )

    def test_instance(self):
        self.assertTrue(isinstance(self.oti,Profile))    

    def test_save_method(self):
        self.oti.save_profile()
        editors = Profile.objects.all()
        self.assertTrue(len(editors) > 0)   
      
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        user = User.objects.create()
        self.oti = Profile(username = user, email = 'test_email',identity = '123456',created = '28-10-2021',updated = '28-10-2021' )
        self.oti.save()
        
        self.new_neighbourhood = Neighbourhood(name = 'test_name',location = 'test_location',occupants = '5000',admin = self.oti)

    def test_instance(self):
            self.assertTrue(isinstance(self.new_neighbourhood,Neighbourhood)) 

    def test_save_method(self):
            self.new_neighbourhood.create_neighbourhood()
            neighbourhood = Neighbourhood.objects.all()
            self.assertTrue(len(neighbourhood) > 0)   

    def tearDown(self):
            Profile.objects.all().delete()
            Neighbourhood.objects.all().delete()

    def test_delete_method(self):
            self.new_neighbourhood.create_neighbourhood()
            self.new_neighbourhood.delete_neighbourhood()
            neighbourhood = Neighbourhood.objects.all()
            self.assertTrue(len(neighbourhood) == 0)     

    def test_update_method(self):
            self.new_neighbourhood.update_neighbourhood()
            neighbourhood = Neighbourhood.objects.all()
            self.assertTrue(len(neighbourhood) > 0) 

    def test_update_occupants__method(self):
            self.new_neighbourhood.update_occupants()
            neighbourhood = Neighbourhood.objects.all()
            self.assertTrue(len(neighbourhood) > 0)    

    def test_find_neighbourhood_by_id(self):
        neighbourhood_id = Neighbourhood.find_neighbourhood()
        self.assertTrue(len(neighbourhood_id) == 0)                                    






