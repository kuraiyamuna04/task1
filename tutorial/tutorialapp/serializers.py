from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def func(self, attrs):
        user = User.objects.get(username=attrs['username'], password=attrs['password'])
        if user is not None:
            return "logged in successfully"
        else:
            return "Wrong Credentials"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password',
                  'email')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user
