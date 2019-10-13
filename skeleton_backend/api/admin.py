from django.contrib import admin
from .models import Profile, Movie, Rating, Tag

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Tag)