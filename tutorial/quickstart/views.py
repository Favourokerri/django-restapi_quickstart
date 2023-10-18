from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from quickstart.serializers import Userserializer, Groupserializer

# Create your views here.
class Usersviewset(viewsets.ModelViewSet):
    """ api for users to be viewed and edithed """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Groupserializer
    permission_classes = [permissions.IsAuthenticated]
