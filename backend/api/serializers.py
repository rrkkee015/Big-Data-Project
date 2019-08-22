from .models import Profile, Movie, Rating
from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class RatingSerializer(DynamicFieldsModelSerializer):
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

class ProfileSerializer(DynamicFieldsModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    rating_fields = ['score', 'movie']
    ratings = RatingSerializer(many=True, fields=rating_fields, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff


class MovieSerializer(DynamicFieldsModelSerializer):
    genres_array = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = '__all__'