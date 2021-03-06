from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient

from .serializers import UserSerializer
from django.core import serializers
from rest_framework.authtoken.models import Token
from django.test import testcases


# class UserProfileAPITest(APITestCase):
# 	def setUp(self):
# 		self.u = User.objects.create_user('test', password='test',
#                                      email='test@test.test')
# 		self.u.save()
# 		user = serializers.serialize("json", User.objects.all().filter(username="test")) 
# 		self.data = {'user': user, 'gender': 'Male', 'dob': '2007-05-09', 'blood_type':'N'}

# 	def test_create_profile(self):
# 		url = reverse('profile-list-list')
		
# 		client = APIClient()
# 		client.force_authenticate(user=self.u)
# 		response = client.post(url, self.data, format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)	

	# def setUp(self):
	# 	superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
	# 	self.client.login(username='john', password='johnpassword')
	# 	User.objects.create(username="mike", first_name="Tyson")
	# 	user = serializers.serialize("json", User.objects.all().filter(username="mike")) 
		
	# 	self.data = {'user': user, 'gender': 'Male', 'dob': '2007-05-09', 'blood_type':'N'}

	# def test_can_create_profile(self):
	# 	url = reverse('profile-list-list')
	# 	response = self.client.post(url, self.data)
	# 	self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	# 	self.assertEqual(UserProfile.objects.count(), 1)
	# 	self.assertEqual(UserProfile.objects.get().gender, 'Male')



	# def test_create_profile(self):
	# 	url = 'profile'
	# 	user = User.objects.create(username='user_test')
	# 	client = APIClient()
	# 	client.force_authenticate(user=user)
	# 	data = {'user': user, 'gender': 'Male', 'dob': '2007-05-09', 'blood_type':'N'}
	# 	response = self.client.post(url, data, format='json')
	# 	self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	# 	self.assertEqual(UserProfile.objects.count(), 1)
	# 	self.assertEqual(UserProfile.objects.get().gender, 'Male')
