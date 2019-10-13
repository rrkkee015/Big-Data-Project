from rest_framework import serializers
from api.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password', 'gender', 'age', 'occupation')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=True,
        )
        profile = Profile.objects.create(
            user=user,
            gender=validated_data.get('gender', ''),
            age=validated_data.get('age'),
            occupation=validated_data.get('occupation', ''),
            expiry_subscribe_date=validated_data.get('expiry_subscribe_date')
        )
        return profile


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError('등록된 사용자가 아닙니다')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = '__all__'


