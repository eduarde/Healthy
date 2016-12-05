from .api import LabViewSet, TestLab
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'labs', TestLab)




urlpatterns = router.urls
