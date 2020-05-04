from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Article
        fields=['id','title','author','email','date','owner']
        #if you want all fields you can do fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','confirm_password']

        def validate(self, data):
            if not data.get('password') or not data.get('confirm_password'):
                raise serializers.ValidationError("Please enter a password and "
                    "confirm it.")

            if data.get('password') != data.get('confirm_password'):
                raise serializers.ValidationError("Those passwords don't match.")

            return data

class UserSerializer(serializers.ModelSerializer):
    articles=serializers.PrimaryKeyRelatedField(many=True,queryset=Article.objects.all())
    class Meta:
        model= User
        fields=['id','username','articles']