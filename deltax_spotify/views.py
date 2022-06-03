from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artists,Songs
from .serializers import ArtistSerializer,SongsSerializer

from .models import Artists
# Create your views here.

class ArtistView(APIView):

    def get(self,request,**kwargs):
        artists = Artists.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

class SongsView(APIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer