from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
import requests
class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        url = "http://localhost:3000/auth/profile"
        headers = {"Authorization":token}
        print(token)
        print(headers)
        if not token:
            return None

        try:
            r = requests.get(url,headers=headers)
            response = r.json()
            print(response)
            username = response['username']
            try:
                print("get user")
                user = User.objects.get(username=username)
            except Exception:
                print("create user")
                user = User.objects.create(username=username)
            print(username)
            print(user)
        except Exception:
            print("disini")
            return None

        return (user, None)