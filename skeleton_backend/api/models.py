from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import Avg

from django.utils import timezone
timezone.now()
import datetime
import pytz
import time


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(default=25, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True)
    subscribe = models.BooleanField(default=False)
    expiry_subscribe_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return "username: {}, gender: {}, age: {}, expiry subscribe date: {}".format(self.user.username, self.gender, self.age, self.expiry_subscribe_date)


#  wrapper for create user Profile
def create_profile(**kwargs):
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        email=kwargs['email'],
        is_active=True,
    )
    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )
    return profile


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    view_count = models.IntegerField()
    imdbId = models.CharField(max_length=10)
    tmdbId = models.CharField(max_length=10)
    youtube_link = models.CharField(max_length=20)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')

    def __str__(self):
        return "{} | {}".format(self.id, self.title)


class Rating(models.Model):
    user = models.ForeignKey(Profile, models.SET_NULL, null=True, related_name='ratings')
    movie = models.ForeignKey(Movie, models.SET_NULL, null=True, related_name='ratings')
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_at = models.DateTimeField()

    def __str__(self):
        return "{} | {} | {}".format(self.user, self.movie, self.rating)


class Tag(models.Model):
    user = models.ForeignKey(Profile, models.SET_NULL, null=True, related_name='tags')
    movie = models.ForeignKey(Movie, models.SET_NULL, null=True, related_name='tags')
    tag = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.tag

