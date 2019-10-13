from django.conf.urls import url
from api.views import auth_views, movie_views, rating_views
from api.views.auth_views import RegistrationAPI, LoginAPI, UserAPI
from api.views.movie_views import MovieListAPI, MovieDetailAPI
from api.views.profile_views import ProfileListAPI, ProfileAPI
from api.views.rating_views import RatingRetrieveUpdateDestroyAPI
from knox import views as knox_views


urlpatterns = [
    url('info/$', movie_views.info),

    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/register/$', RegistrationAPI.as_view()),
    url('auth/login/$', LoginAPI.as_view()),
    url('auth/logout/$', knox_views.LogoutView.as_view(), name="knox_logout"),
    url('auth/user/$', UserAPI.as_view()),

    url('movies/$', MovieListAPI.as_view(), name='movie_list'),
    url('movies/(?P<pk>[\d]+)/$', MovieDetailAPI.as_view(), name='movie_list'),
    url('movies/random/$', movie_views.randomMovie),

    url('profiles/$', ProfileListAPI.as_view()),
    url('profiles/(?P<username>[\w]+)/$', ProfileAPI.as_view()),

    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('ratings/(?P<pk>[\d]+)/$', RatingRetrieveUpdateDestroyAPI.as_view()),
]


