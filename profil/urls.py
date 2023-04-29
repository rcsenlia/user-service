from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')
router.register('relationship',RelationshipViewSet,basename='relationship')
router.register('genre',GenreViewSet,basename='genre')
router.register('hobi',HobiViewSet,basename='hobi')
urlpatterns = [
    path('', include(router.urls)),
    
]