from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artists(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    bio = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.name)

class Songs(models.Model):
    name = models.CharField(max_length=100)
    date_of_release = models.DateField()
    cover_image = models.ImageField(upload_to ='uploads/')
    artists = models.ManyToManyField(Artists,null=True,blank=True,related_name='Songs')
    def __str__(self):
        return str(self.name)

class Rating(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Songs,null=True,blank=True,on_delete=models.CASCADE,related_name='rating')
    rating = models.IntegerField(choices=RATINGS,default=0)
    def __str__(self):
        return str(self.song.name)
