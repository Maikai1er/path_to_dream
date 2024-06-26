from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StepViewSet

router = DefaultRouter()
router.register(r'steps', StepViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
