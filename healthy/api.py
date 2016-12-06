from rest_framework import viewsets, generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer, LabSerializer, MarkerSerializer, LabResultSerializer, MarkerPredefinedSerializer, DictionarySerializer, LabNoteSerializer
from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote





class UserProfileViewSet(viewsets.ModelViewSet):
	serializer_class = UserProfileSerializer

	def get_queryset(self):
		return UserProfile.objects.all().filter(user=self.request.user)





class LabViewSet(viewsets.ModelViewSet):
	serializer_class = LabSerializer

	# def pre_save(self, obj):
 #        obj.user = self.request.user

	def get_queryset(self):
		return Lab.objects.all().filter(user=self.request.user).order_by('-pk')





class DictionaryViewSet(viewsets.ModelViewSet):
	queryset = Dictionary.objects.all()
	http_method_names = [u'get']
	serializer_class = DictionarySerializer





class LabResultViewSet(viewsets.ModelViewSet):
	serializer_class = LabResultSerializer
	# lookup_field = 'lab_ref'

	# def get_lab(self, lab):
	# 	return get_object_or_404(Lab, pk=self.kwargs.get("lab"))

	def get_queryset(self):
		return LabResult.objects.all()








	