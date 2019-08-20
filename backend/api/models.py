from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.user)

#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
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

    @property
    def genres_array(self):
        return self.genres.strip().split('|')

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'ratings')
    user = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'ratings')
    score = models.IntegerField(
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        default = 5
    )
    date = models.DateTimeField()

    def __str__(self):
        return '영화 : {} 평점 : {} 작성자 : {}'.format(self.movie, self.score, self.user)
