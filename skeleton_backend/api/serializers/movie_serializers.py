from rest_framework import serializers
from api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    average_rating = serializers.DecimalField(max_digits=2, decimal_places=1)
    rating_numbers = serializers.IntegerField()
    tags = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'average_rating', 'rating_numbers', 'view_count', 'imdbId', 'tmdbId', 'youtube_link', 'tags')


class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'