from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Profile, Movie
from api.serializers.rating_serializers import RatingSerializer
from rest_framework.response import Response
from django.conf import settings
import datetime

# json data
total_result = {

}

@api_view(['GET'])
def cluster_user_kmeans(request):
    global final_result

    total_result = {
        "algorithm": "",
        "total_clusters": []
    }
    k = request.GET.get('k')
    max_iter = request.GET.get('max_iter')
    n_init = request.GET.get('n_init')
    do_cluster(k, max_iter, n_init)
    
    return Response(total_result, status=status.HTTP_200_OK)


@api_view(['GET'])
def cluster_user_hc(request):
    global final_result

    total_result = {
        "algorithm": "",
        "total_clusters": []
    }
    n_clusters = request.GET.get('n_clusters')
    linkage = request.GET.get('linkage')


@api_view(['GET'])
def cluster_user_em(request):
    global final_result

    total_result = {
        "algorithm": "",
        "total_clusters": []
    }

    n_components = request.GET.get('n_components')
    covariance_type = request.GET.get('covariance_type')


# 유사한 User 추천 알고리즘
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import mixture
from sklearn.preprocessing import MultiLabelBinarizer
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
import pandas as pd
import random
import math
import json

mlb = MultiLabelBinarizer()

user = None
user_userId = None
user_final = None


clusters = []
cluster_users = []

def do_cluster():
    global user, user_userId, user_final, users

    '''데이터 전처리'''
    movies_data = pd.read_csv('data_movies.dat', sep='::', names=['movie_id', 'title', 'genres'], engine='python')
    ratings_data = pd.read_csv('data_ratings.dat', sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'], engine='python')
    users = pd.read_csv('data_users.dat', sep='::', names=['user_id', 'gender', 'age', 'occupation', 'zip_code'], engine='python')

    # clustering에 사용할 user data
    user = pd.DataFrame(users.drop('zip_code', axis=1))
    # 나중에 합칠 user_id dataframe
    user_userId = pd.DataFrame(user['user_id'], columns = ['user_id'])
    user = user.drop('user_id', axis=1)
    # encoding
    user = pd.get_dummies(user, columns=["gender", "age", "occupation"], prefix=["gender", "age", "occupation"])

    user_KMeans(5, 300, 10)
    user_EM(5, 'full')
    user_HC(5, 'ward')

    user_final = user_userId


def user_KMeans(user_k=5, user_max_iter=300, user_n_init=10):
    global user_userId

    model_km = KMeans(n_clusters=user_k, max_iter=user_max_iter, n_init=user_n_init)
    model_km.fit(user.values)
    df_kmeans = pd.DataFrame(model_km.labels_, columns = ['KMeans'])
    user_userId = user_userId.join(df_kmeans)


def user_EM(user_n_components=5, user_covariance_type='full'):
    global user_userId

    model_em = mixture.GaussianMixture(n_components=user_n_components, covariance_type=user_covariance_type)
    user_userId['EM'] = model_em.fit_predict(user.values)


def user_HC(user_n_clusters=5, user_linkage='ward'):
    global user_userId

    model_hc = AgglomerativeClustering(n_clusters=user_n_clusters, linkage=user_linkage)
    model_hc.fit(user.values)
    df_hc = pd.DataFrame(model_hc.labels_, columns = ['HC'])
    user_userId = user_userId.join(df_hc)

do_cluster()
print(user_final)

def extract_user(user_id, clust_method):
    global same_clust_user

    # user_id = int(input())
    # clust_method = input()

    # user가 속한 cluster
    user_clust = user_final[user_final.user_id == user_id][clust_method].values[0]
    print(user_clust)

    if clust_method == 'KMeans':
        user_list = user_final[user_final.KMeans == user_clust]
    elif clust_method == 'EM':
        user_list = user_final[user_final.EM == user_clust]
    elif clust_method == 'HC':
        user_list = user_final[user_final.HC == user_clust]
    
    same_clust_user = pd.merge(user_list, users, on = 'user_id')

# extract_user(777, 'HC')
# print(same_clust_user)