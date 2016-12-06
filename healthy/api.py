from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializers import UserProfileSerializer, LabSerializer, MarkerSerializer, LabResultSerializer, MarkerPredefinedSerializer, DictionarySerializer, LabNoteSerializer
from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote





class LabViewSet(viewsets.ModelViewSet):
	serializer_class = LabSerializer

	def get_queryset(self):
		
		return Lab.objects.all().filter(user=self.request.user).order_by('-pk')


	