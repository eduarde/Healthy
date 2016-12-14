from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer, LabSerializer, MarkerSerializer, LabResultSerializer, MarkerPredefinedSerializer, DictionarySerializer, LabNoteSerializer, UserSerializer
from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote





class UserProfileViewSet(viewsets.ModelViewSet):
	serializer_class = UserProfileSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return UserProfile.objects.all().filter(user=self.request.user)





class LabViewSet(viewsets.ModelViewSet):
	serializer_class = LabSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Lab.objects.all().filter(user=self.request.user).order_by('-pk')





class DictionaryViewSet(viewsets.ModelViewSet):
	queryset = Dictionary.objects.all()
	http_method_names = [u'get']
	serializer_class = DictionarySerializer
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
	# permission_classes = (IsAuthenticated,)





class LabResultViewSet(viewsets.ModelViewSet):
	serializer_class = LabResultSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def perform_create(self,serializer):

		marker_ref = Marker.objects.get(name=serializer.validated_data['marker_ref'])
		serializer.save(lab_ref=self.get_lab(), predefined_ref=self.get_marker_predefined(marker_ref))


	def get_marker_predefined(self,marker):
		
		lab = self.get_lab()
		age = lab.user_age_lab

		marker_pred = ""

		if marker.variant_type == "Gender":
			user = self.request.user
			gender = UserProfile.objects.filter(user=user)[:1].get().gender

			if age < MarkerPredefined.CHILD_AGE_THRESHOLD:
				marker_pred = MarkerPredefined.objects.all().filter(marker_ref=marker,variant_gender="Child")[:1].get()

			if not marker_pred:
				marker_pred = MarkerPredefined.objects.all().filter(marker_ref=marker,variant_gender=gender)[:1].get()

		# elif marker.variant_type == "Age":
		# 	variant_type = age
		else:
			marker_pred = MarkerPredefined.objects.get(marker_ref=marker)
		return marker_pred
	


	def get_lab(self):
		return get_object_or_404(Lab, pk=self.kwargs.get("lab"))

	def get_queryset(self):
		return LabResult.objects.all().filter(lab_ref=self.get_lab())








	