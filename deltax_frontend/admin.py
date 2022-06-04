from django.contrib import admin

# Register your models here.
from .models import Artists,Songs,Rating
# Register your models here.

admin.site.register(Artists)
admin.site.register(Songs)
admin.site.register(Rating)
