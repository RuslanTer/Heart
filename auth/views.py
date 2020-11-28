from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, GroupSerializer
from Heart.resources.value_parse import create_rows


class UserViewSet(viewsets.ModelViewSet):
    create_rows()



