from django.urls import path, include
from .views import JobViewSet, create_application
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='Jobs')

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/<int:pk>/applications', create_application)
]