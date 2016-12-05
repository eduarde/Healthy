from django.contrib import admin
from .models import UserProfile, Lab, Marker, LabResult, MarkerPredefined, Dictionary, LabNote

admin.site.register(UserProfile)
admin.site.register(Lab)
admin.site.register(Marker)
admin.site.register(LabResult)
admin.site.register(MarkerPredefined)
admin.site.register(Dictionary)
admin.site.register(LabNote)

