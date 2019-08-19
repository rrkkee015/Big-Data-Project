from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating

@api_view(['GET', 'POST', 'DELETE'])
def rating(request):

  if request.method == 'GET':
    movieid = request.GET.get('id', None)
    username = request.GET.get('username', None)
    rating = request.GET.get('rating', None)
    date = request.GET.get('date', None)

    rating = Rating.object.all()
