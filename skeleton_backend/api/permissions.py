from rest_framework import permissions
from api.models import Profile

class IsSubscriber(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.subscribe


class IsAuthenticatedAndUserOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        profile = Profile.objects.filter(user=request.user).exists()
        return profile

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user