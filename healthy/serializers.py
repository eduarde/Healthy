from rest_framework import serializers

from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote





class UserProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfile
		fields = '__all__'





class LabSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Lab
		fields = ('user', 'date', 'ref_number', 'doctor', 'collection_point', 'patient_code', 'user_age_lab', 'abnormal_lab')






class MarkerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Marker





	
class LabResultSerializer(serializers.ModelSerializer):


	class Meta:
		model = LabResult
		fields = ( 'marker_ref', 'predefined_ref', 'value')





class MarkerPredefinedSerializer(serializers.ModelSerializer):

	class Meta:
		model = MarkerPredefined





class DictionarySerializer(serializers.ModelSerializer):

	class Meta:
		model = Dictionary
		fields = '__all__'






class LabNoteSerializer(serializers.ModelSerializer):

	class Meta:
		model = LabNote

