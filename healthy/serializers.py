from rest_framework import serializers

from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'





class UserProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UserProfile
		fields = '__all__'





class LabNoteSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = LabNote
		fields = ('comment','pub_date')





class LabSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Lab
		fields = ('pk', 'user', 'date', 'ref_number', 'doctor', 'collection_point', 'patient_code', 'user_age_lab', 'abnormal_lab')






class MarkerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Marker
		fields = ('name', 'abbr', 'category','um')
		read_only_fields = ('abbr','category','um')




    	

class MarkerPredefinedSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = MarkerPredefined
		fields = ('name','threshold_min','threshold_max')
		read_only_fields = ('threshold_min','threshold_max',)





class LabResultSerializer(serializers.ModelSerializer):

	marker_ref = MarkerSerializer()
	predefined_ref = MarkerPredefinedSerializer()

	class Meta:
		model = LabResult
		fields = ( 'marker_ref', 'value','lab_ref','predefined_ref','abnormal_result')
	




class DictionarySerializer(serializers.ModelSerializer):
	marker_ref = MarkerSerializer()

	class Meta:
		model = Dictionary
		fields = ('id','marker_ref','text')








