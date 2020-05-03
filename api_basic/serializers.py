from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','author','email','date']
        #if you want all fields you can do fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

def check(User):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        validators=[
            check
        ]