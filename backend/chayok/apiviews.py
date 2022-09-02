from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Tea, TeaImages
from  .serializers import TeaSerializer

class TeaList(generics.ListCreateAPIView):
    queryset = Tea.objects.all()
    serializer_class = TeaSerializer

class TeaDetail(generics.RetrieveDestroyAPIView):
    queryset = Tea.objects.all()
    serializer_class = TeaSerializer

class CreateTea(generics.CreateAPIView):
    serializer_class = TeaSerializer

class DestroyTea(generics.DestroyAPIView):
    serializer_class = TeaSerializer

class UpdateTea(generics.UpdateAPIView):
    serializer_class = TeaSerializer