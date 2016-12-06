from .api import  LabViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'labs', LabViewSet, 'LabViewSet')
urlpatterns = router.urls