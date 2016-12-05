from rest_framework import serializers

from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote





class UserProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfile




class LabSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lab
		fields = '__all__'




class MarkerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Marker





class LabResultSerializer(serializers.ModelSerializer):

	class Meta:
		model = LabResult





class MarkerPredefinedSerializer(serializers.ModelSerializer):

	class Meta:
		model = MarkerPredefined





class DictionarySerializer(serializers.ModelSerializer):

	class Meta:
		model = Dictionary




class LabNoteSerializer(serializers.ModelSerializer):

	class Meta:
		model = LabNote

