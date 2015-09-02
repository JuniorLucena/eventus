from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics

from api.permissions import IsOwner
from api.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner,)
