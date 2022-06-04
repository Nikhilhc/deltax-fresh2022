from rest_framework import serializers
from .models import Artists,Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['name','dob','bio']

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('name','date_of_release','cover_image','artists','rating')