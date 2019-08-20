from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.response import Response

@api_view(['GET'])
def profiles(request):

  if request.method =='GET':
    id = request.GET.get('id', None)
    user = request.GET.get('user', None)
    gener = request.GET.get('gender', None)
    age = request.GET.get('age', None)
    occupation = request.GET.get('occupation', None)

    profiles = Profile.objects.all()

    serializer = ProfileSerializer(profiles, many=True)
    
    return Response(data=serializer.data, status=status.HTTP_200_OK)