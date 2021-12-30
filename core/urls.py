from rest_framework.routers import SimpleRouter

from core.views import UserModelViewSet

router = SimpleRouter()
router.register('users', UserModelViewSet, basename='users')

urlpatterns = router.urls
