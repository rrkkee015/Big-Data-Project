from django.contrib import admin
from .models import Movie, Rating, Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)