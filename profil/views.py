from django.shortcuts import render
import datetime

from django.forms.models import model_to_dict
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializer
from .models import Profile
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_class = ['get', 'post', 'put', 'delete']

    @action(detail=True, methods=['get'])
    def get_profile_id(self, request, id=None):
        user = request.user
        profile = Profile.objects.filter(id=pk)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)