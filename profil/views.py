from django.shortcuts import render
import datetime

from django.forms.models import model_to_dict
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import ProfileSerializer,HobiSerializer,GenreSerializer,RelationshipSerializer,UserSerializer,HobiIdSerializer,ProfileOnlySerializer
from .models import Profile,Hobi,Genre,Relationship
from userauth.auth import UserAuthentication
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    authentication_classes = [UserAuthentication]

    @action(detail = False)
    def get_my_profile(self,request):
        user = request.user
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)

    @action(detail = False,methods=['post'],serializer_class=UserSerializer)
    def post_profile_username(self, request):
        username = request.data.get('username',None)
        if(username == None):
            return Response({"username":"This field is required"},status=400)
        profile = Profile.objects.filter(user__username=username)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def update_profile_username(self,request):
        user = request.user
        data = request.data
        gender = data.get('gender',None)
        deskripsi =  data.get('deskripsi',None)
        domisili = data.get('domisili',None)
        umur = data.get('umur',None)
        cek = ProfileOnlySerializer(data=data)
        cek.is_valid(raise_exception=True)
        if(gender):
            user.profile.gender = gender
        if(deskripsi):
            user.profile.deskripsi = deskripsi
        if(domisili):
            user.profile.domisili = domisili
        if(umur):
            user.profile.umur = umur
        user.profile.save()
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)
    @action(detail=False,methods=['post'])
    def add_hobi(self,request):
        
        hobi_id = request.data.get('hobi',None)
        if(hobi_id == None):
            return Response({"hobi":"this field is required"},status=400)
        try :
            user = request.user
            for id in hobi_id :
                hobi = Hobi.objects.get(id=id)
                user.profile.hobi.add(hobi)
        except TypeError:
            return Response({"hobi":"hobi is type list of int (the id of hobi)"},status=401)
        user.profile.save()
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)
    @action(detail=False,methods=['post'])
    def add_genre(self,request):
        genre_id = request.data['genre']
        if(genre_id == None):
            return Response({"genre":"this field is required"},status=400)
        try :
            user = request.user
            for id in genre_id:
                genre = Genre.objects.get(id=id)
                user.profile.genre.add(genre)
        except TypeError:
            return Response({"hobi":"hobi is type list of int (the id of hobi)"},status=401)
        user.profile.save()
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_teman(self,request):
        user = request.user
        username = request.data.get('username',None)
        if(username == None):
            return Response({"username":"This field is required"},status=400)
        
        try :
            teman = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response({"error":"user not found"},status=401)
        user.profile.teman.add(teman)
        user.profile.save()
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data)
    @action(detail=False)
    def get_my_friend(self,request):
        user = request.user
        serializer = UserSerializer(user.profile.teman,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def get_friend_username(self,request):
        username = request.data.get('username',None)
        if(username == None):
            return Response({"username":"This field is required"},status=400)
        try :
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response({"error":"user not found"},status=401)
        serializer = UserSerializer(user.profile.teman,many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def get_friended(self,request):
        user = request.user
        teman = Relationship.objects.filter(user__id=user.id)
        print(teman.values())
        data = []
        for x in teman :
            temp = User.objects.get(id = x.profile.user.id)
            data += [temp]
        
        serializer = UserSerializer(data,many=True)
        return Response(serializer.data)
    # @action(detail=True, methods=['get'])
    # def remove_my_friend(self,request):

class HobiViewSet(viewsets.ModelViewSet):
    queryset = Hobi.objects.all()
    serializer_class = HobiSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    authentication_classes = [UserAuthentication]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    authentication_classes = [UserAuthentication]

class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    authentication_classes = [UserAuthentication]