from rest_framework import generics
from django.shortcuts import get_object_or_404
from api.models import Profile
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.permissions import IsAuthenticatedAndUserOnly
from api.serializers.profile_serializers import (
    ProfileSerializer,
    ProfileDetailSerializer
)


class ProfileListAPI(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAPI(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedAndUserOnly|IsAdminUser]

    def get_object(self):
        profile = get_object_or_404(Profile, user__username=self.kwargs['username'])
        return profile

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
