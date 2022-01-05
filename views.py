from django.shortcuts import render
from .serializers import testSerializers
from.models import test
from rest_framework import status,permissions,generics,viewsets

class StudentCurd(viewsets.ModelViewSet):
    queryset=test.objects.all()
    serializer_class=testSerializers
    permission_classes=[permissions.AllowAny]



# Create your views here.
