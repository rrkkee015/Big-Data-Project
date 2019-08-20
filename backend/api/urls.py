from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import ratings_views
from api.views import profiles_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', ratings_views.ratings, name='ratings'),
    url('profiles/$', profiles_views.profiles, name='profiles')
]
