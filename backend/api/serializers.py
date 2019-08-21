from .models import Profile, Movie, Rating
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    # movie = serializers.CharField()
    # user = serializers.CharField()

    movie = serializers.SerializerMethodField('get_movie')
    user = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Rating
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.user.username

    def get_movie(self, obj):
        return obj.movie.title

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = '__all__'