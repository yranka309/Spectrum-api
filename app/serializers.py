from rest_framework import serializers
#from .models import UserProfile,UserToken
from django.contrib.auth.models import User

""" class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('user','name','admission','branch','phone','coins')

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'
 """