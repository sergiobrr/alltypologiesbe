from rest_framework import routers
from .views import ProjectViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register('projects', ProjectViewSet)

urlpatterns = [
    url('', include(router.urls))
]

