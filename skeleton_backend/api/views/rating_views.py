from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.models import Rating, Profile, Movie
from api.serializers.rating_serializers import RatingSerializer
from rest_framework.response import Response

import datetime


class RatingRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        rating = get_object_or_404(Rating, pk=self.kwargs['pk'])
        return rating

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


@api_view(['POST'])
def ratings(request):
    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for rating in ratings:
            userId = rating.get('userId', None)
            if userId:
                user = Profile.objects.get(id=int(userId))
            movieId = rating.get('movieId', None)
            if movieId:
                movie = Movie.objects.get(id=int(movieId))

            score = rating.get('rating', None)
            timeStamp = rating.get('timeStamp', None)
            created_at = datetime.datetime.fromtimestamp(int(timeStamp))
            Rating(user=user, movie=movie, rating=round(float(score),1), created_at=created_at).save()

        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        pass
    