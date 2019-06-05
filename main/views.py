from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.urls import reverse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from oauth2_provider.views import ProtectedResourceView
from rest_framework import generics, permissions

from main.serializers import UserSerializer, GroupSerializer


def index(request):
    return JsonResponse({
            "message": "Hello world!",
            "logout": request.build_absolute_uri(reverse("logout"))
        })


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                "error": "please log in!"
            }, status=403)

        return JsonResponse({
            "message": "Hello world!",
            "logout": request.build_absolute_uri(reverse("logout"))
        })


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

