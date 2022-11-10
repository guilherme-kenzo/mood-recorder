from .views import MoodViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("mood", MoodViewset)

urlpatterns = router.urls