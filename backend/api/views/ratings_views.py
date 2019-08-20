from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Movie, Profile
from api.serializers import RatingSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def ratings(request):

  if request.method == 'GET':
    movie = request.GET.get('movieid', None)
    user = request.GET.get('userid', None)
    score = request.GET.get('score', None)
    date = request.GET.get('date', None)

    ratings = Rating.objects.all()

    serializer = RatingSerializer(ratings, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

  if request.method == 'POST':
    ratings = request.data.get('ratings', None)
    for rating in ratings:
      movie = rating.get('movieid', None)
      if movie:
        movie = Movie.objects.get(id=int(movie))
      user = rating.get('userid', None)
      if user:
        user = Profile.objects.get(id=int(user))
      score = rating.get('score', None)
      date = rating.get('date', None)

      Rating(movie = movie, user = user, score = score, date = date).save()

    return Response(status=status.HTTP_200_OK)