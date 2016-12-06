from .api import  LabViewSet, UserProfileViewSet, DictionaryViewSet, LabResultViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'dictionary', DictionaryViewSet, "Dictionary")
router.register(r'profile', UserProfileViewSet, "UserProfileViewSet")
router.register(r'labs', LabViewSet, 'LabViewSet')
router.register(r'labresults',LabResultViewSet,'LabResults')

urlpatterns = router.urls