from rest_framework.routers import DefaultRouter
from mainapp.views import ClientViewSet

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='cliente')
