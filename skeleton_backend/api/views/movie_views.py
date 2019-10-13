from rest_framework import status, generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view
from api.models import Profile, Movie, Rating
from api.serializers.movie_serializers import MovieSerializer
from rest_framework.response import Response

from django.db.models import F
from django.db.models import Avg, Count, Max
import random


@api_view(['GET'])
def info(request):
    user_cnt = Profile.objects.count()
    movie_cnt = Movie.objects.count()
    rating_cnt = Rating.objects.count()
    return Response({
        "user_cnt": user_cnt,
        "movie_cnt": movie_cnt,
        "rating_cnt": rating_cnt
    })


@api_view(['GET'])
def randomMovie(request):
    movies = Movie.objects.annotate(average_rating=Avg('ratings__rating')).annotate(rating_numbers=Count('ratings'))
    max_id = movies.aggregate(max_id=Max("id"))['max_id']
    queryset = []
    cnt = request.query_params.get('cnt')
    if cnt:
        while int(cnt) > 0:
            pk = random.randint(1, max_id)
            if movies.filter(pk=pk).exists():
                queryset.append(movies.filter(pk=pk).first())
                cnt -= 1
    else:
        cnt = 8
        while cnt > 0:
            pk = random.randint(1, max_id)
            if movies.filter(pk=pk).exists():
                queryset.append(movies.filter(pk=pk).first())
                cnt -= 1
    serializer = MovieSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class MovieListAPI(generics.ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.annotate(average_rating=Avg('ratings__rating')).annotate(rating_numbers=Count('ratings'))
    serializer_class = MovieSerializer


class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    queryset = Movie.objects.annotate(average_rating=Avg('ratings__rating')).annotate(rating_numbers=Count('ratings'))
    serializer_class = MovieSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ('PUT', 'DELETE'):
            self.permission_classes = [IsAdminUser]
        return super(self.__class__, self).get_permissions()





# @api_view(['GET', 'POST', 'DELETE'])
# def movieList(request):

#     if request.method == 'GET':
#         id = request.GET.get('id', request.GET.get('movie_id', None))
#         title = request.GET.get('title', None)
#         genre = request.GET.get('genre', None)
#         rating = request.GET.get('rating', None)
        
#         movies = Movie.objects.annotate(average_rating=Avg('ratings__rating')).annotate(rating_numbers=Count('ratings'))

#         if id:
#             movies = movies.filter(pk=id)
#         if title:
#             movies = movies.filter(title__icontains=title)
#         if genre:
#             movies = movies.filter(genres__icontains=genre)
#         if rating:
#             if rating.lower() == 'desc':
#                 movies = movies.order_by('-average_rating')
#             elif rating.lower() == 'asc':
#                 movies = movies.order_by('average_rating')

#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'DELETE':
#         movie = Movie.objects.all()
#         movie.delete()
#         return Response(status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         movies = request.data.get('movies', None)
#         for movie in movies:
#             id = movie.get('id', None)
#             title = movie.get('title', None)
#             genres = movie.get('genres', None)

#             if not (id and title and genres):
#                 continue
#             if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
#                 continue

#             Movie(id=id, title=title, genres='|'.join(genres)).save()

#         return Response(status=status.HTTP_200_OK)
