from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artists,Songs
from .serializers import ArtistSerializer,SongsSerializer

from .models import Artists
# Create your views here.

class ArtistView(APIView):

    def get(self,request,**kwargs):
        artists = Artists.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        Create Artists
        '''
        data = {
            'name': request.data.get('name'),
            'dob': request.data.get('dob'),
            'bio': request.data.get('bio')
        }
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongsView(APIView):

    def get(self,request,**kwargs):
        artists = Songs.objects.all()
        serializer = SongsSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        Create Artists
        '''
        data = {
            'name': request.data.get('name'),
            'date_of_release': request.data.get('dob'),
            'cover': request.data.get('bio')
        }
        serializer = SongsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)