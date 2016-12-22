from .api import  LabViewSet, UserProfileViewSet, DictionaryViewSet, LabResultViewSet, NoteViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'dictionary', DictionaryViewSet, "dictionary-list")
router.register(r'profile', UserProfileViewSet, "profile-list")
router.register(r'labs', LabViewSet, 'labs-list')
router.register(r'lab/(?P<lab>\d+)/results',LabResultViewSet,'lab-results') # lab/<pk>/results/
router.register(r'lab/(?P<lab>\d+)/notes',NoteViewSet,'lab-notes')



urlpatterns = router.urls