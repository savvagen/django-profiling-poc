from rest_framework.routers import DefaultRouter
from .views import SentryPerformanceViewSet

app_name = "performance"

router = DefaultRouter()
router.register(r'performance', SentryPerformanceViewSet, basename='performance')

urlpatterns = router.urls
