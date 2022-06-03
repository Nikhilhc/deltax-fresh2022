from django.db import models

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
    artists = models.ForeignKey(Artists,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)