from rest_framework import serializers
from api.models import Rating
from api.serializers.movie_serializers import UserMovieSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class UserRatingSerializer(serializers.ModelSerializer):
    movie = UserMovieSerializer()
    class Meta:
        model = Rating
        # fields = '__all__'
        fields = ('id', 'movie', 'rating')