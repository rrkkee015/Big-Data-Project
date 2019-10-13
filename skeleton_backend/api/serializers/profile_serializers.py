from rest_framework import serializers
from api.models import Profile
from api.serializers.auth_serializers import UserSerializer
from api.serializers.rating_serializers import UserRatingSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'age', 'occupation')


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    ratings = UserRatingSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'gender', 'age', 'occupation', 'ratings')