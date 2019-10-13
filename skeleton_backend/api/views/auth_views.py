from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Profile, create_profile
from api.serializers.auth_serializers import (
        ProfileSerializer,
        CreateUserSerializer,
        UserSerializer,
        ProfileSerializer,
        LoginUserSerializer
)
from knox.models import AuthToken


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(
            {
                "profile": ProfileSerializer(profile, context=self.get_serializer_context()).data,
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        profile = Profile.objects.get(user=user)
        return Response(
            {
                "profile": ProfileSerializer(profile, context=self.get_serializer_context()).data,
                "user": {
                    "username": user.username,
                    "token": AuthToken.objects.create(user)[1],
                }
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        return Response(
            {
                'profile': ProfileSerializer(profile, context=self.get_serializer_context()).data,
                'username': profile.user.username
            }
        )

@api_view(['POST'])
def signup_many(request):
    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def users(request):

    if request.method == 'GET':
        id = request.GET.get('id', None)

        users = Profile.objects.all()

        if id:
            users = users.filter(pk=id)

        serializer = ProfileSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)