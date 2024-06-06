from django.urls import path
from .views import *

urlpatterns = [
    path('',frontpage ,name='frontpage'),
    path('views_showcase/<str:pk>/',views_showcase ,name='views_show'),
    path('views_lastmovies/<str:pk>/',views_lastmovies ,name='views_lastmovies'),
    path('views_movies/<str:pk>',views_movies,name='views_movies')

]
