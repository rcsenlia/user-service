from .models import Profile,Hobi,Genre,Relationship
from rest_framework import serializers
from django.contrib.auth.models import User


class HobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobi
        fields = "__all__"

class HobiIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobi
        fields = ['id']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    hobi = HobiSerializer(many=True)
    genre = GenreSerializer(many=True)
    teman = UserSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileOnlySerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = ['gender','deskripsi','domisili','umur']