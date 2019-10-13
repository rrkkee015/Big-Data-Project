from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Profile, Movie
from rest_framework.response import Response
from django.conf import settings

import datetime

# json화 데이터
total_result = {
    "algorithm": "",
    "total_clusters": []
} 


@api_view(['GET'])
def cluster_movie_kmeans(request):
    global total_result
    # 초기화
    total_result = {
        "algorithm": "",
        "total_clusters": []
    }
    k = request.GET.get("k")
    max_iter = request.GET.get("max_iter")
    n_init = request.GET.get("n_init")
    do_cluster(k,max_iter,n_init)
    # print(total_result)
    return Response(total_result, status=status.HTTP_200_OK)


# 알고리즘
# -*- encoding: utf-8 -*-

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import mixture
from sklearn.preprocessing import MultiLabelBinarizer 
mlb = MultiLabelBinarizer()

from functools import reduce

import joblib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

movie_result = None
movies = None
ratings_result = None


clusters = []
cluster_genres = []
cluster_movies = []

def make_clusters(k):
    for i in range(k):
        cluster = movie_result[movie_result.movie_cluster==i]
        cluster = cluster.drop('movie_title', axis=1)
        cluster = cluster.drop('movie_genres',axis=1)
        cluster = cluster.drop('movie_cluster',axis=1)
        clusters.append(cluster)

def make_cluster_infos(k):
    global total_result
    for i in range(k):
        cluster_genre = clusters[i].sum()
        cluster_genre = cluster_genre.sort_values(ascending=False)
        cluster_genre = pd.DataFrame(cluster_genre, columns=['count'])
        cluster_genre = cluster_genre[1:4]
        cluster_genres.append(cluster_genre)
        total_result['total_clusters'].append({
            "cluster_genres": cluster_genre.to_dict()
        })

        cluster_movie = pd.merge(ratings_result, clusters[i], on='movie_id')
        cluster_movie = cluster_movie.sort_values(by=['all_ratings','rating_avg'], ascending=False)
        cluster_movie = cluster_movie[:50]
        cluster_movie = cluster_movie[['movie_id','rating_avg','all_ratings']]
        cluster_movie.reset_index().drop('index', axis=1)
        cluster_movie = pd.merge(movies, cluster_movie, on='movie_id')
        cluster_movie.sort_values(by=['all_ratings','rating_avg'], ascending=False)
        total_result['total_clusters'][i]["cluster_movies"] = cluster_movie.to_dict('records')
    


def do_cluster(user_k=6,user_max_iter=300,user_n_init=10):
    global movie_result, movies, ratings_result, total_result
    print(len(total_result["total_clusters"]))
    user_k = int(user_k)
    user_max_iter = int(user_max_iter)
    user_n_init = int(user_n_init)

    '''데이터 전처리'''

    movies = pd.read_csv(settings.MEDIA_ROOT, sep='::', names=['movie_id', 'movie_title', 'movie_genres'], engine='python')
    mdfc =  movies.drop('movie_title', axis=1)
    mdfc = mdfc.drop('movie_id', axis=1)
    mdfc['movie_genres'] = mdfc['movie_genres'].str.split('|')
    mdfc = pd.DataFrame(mlb.fit_transform(mdfc.pop('movie_genres')), columns=mlb.classes_, index=mdfc.index)

    '''클러스터링'''

    movie_model = KMeans(n_clusters=user_k, max_iter=user_max_iter, n_init=user_n_init)
    movie_model.fit(mdfc.values)
    total_result['algorithm'] = str(movie_model)
    movie_result = movies.join(pd.DataFrame(movie_model.labels_, columns = ['movie_cluster']))
    movie_result = movie_result.join(mdfc)

    '''데이터 분석'''
    ratings_data = pd.read_csv('~/data_ratings.dat', sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
    ratings_data = ratings_data.drop('user_id', axis=1)
    ratings_data = ratings_data.drop('timestamp', axis=1)

    ratings_result = ratings_data.groupby(['movie_id'], as_index=False).mean()
    ratings_result.rename(columns={'rating':'rating_avg'}, inplace=True)
    ratings_counts = ratings_data.groupby(['movie_id'], as_index=False).count()
    ratings_result["all_ratings"] = ratings_counts["rating"] 

    make_clusters(user_k)
    make_cluster_infos(user_k)
    print(len(total_result["total_clusters"]))
