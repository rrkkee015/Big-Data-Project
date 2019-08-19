from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
]
