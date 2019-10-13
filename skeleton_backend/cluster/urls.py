from django.conf.urls import url
from cluster.views import cluster_views


urlpatterns = [
    url('movie/kmeans/$', cluster_views.cluster_movie_kmeans, name='cluster_movie_kmeans'),
]
