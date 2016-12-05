from rest_framework import viewsets


from .serializers import UserProfileSerializer, LabSerializer, MarkerSerializer, LabResultSerializer, MarkerPredefinedSerializer, DictionarySerializer, LabNoteSerializer
from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote



# class LabViewSet(viewsets.ViewSet):

# 	def list(self, request):
# 		queryset = Lab.objects.all().filter(user=self.request.user).order_by('-pk')
# 		serializer = LabSerializer
# 		return Response(serializer.data)

# 	def retrieve(self, request, pk=None):
# 		queryset = Lab.objects.all().filter(user=self.request.user).order_by('-pk')
# 		lab = get_object_or_404(queryset, pk=pk)
# 		serializer = LabSerializer
# 		return Response(serializer.data)



class TestLab(viewsets.ModelViewSet):
	queryset = Lab.objects.all()
	serializer_class = LabSerializer