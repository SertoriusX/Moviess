from django.urls import path
from .views import *

urlpatterns = [
    # showcase movies urls
    path('admin_create_showcase/',admin_create_showcase,name='admin_create_showcase'),
    path('admin_views_showcase/<str:pk>/',admin_views_showcase,name='admin_views_showcase'),
    path('admin_update_showcase/<str:pk>/',admin_update_showcase,name='admin_update_showcase'),
    path('admin_delete_showcase/<str:pk>/',admin_delete_showcase,name='admin_delete_showcase'),
    #last movies urls
    path('admin_create_lastmovies/',admin_create_lastmovies,name='admin_create_lastmovies'),
    path('admin_views_lastmovies/<str:pk>/',admin_views_lastmovies,name='admin_views_lastmovies'),
    path('admin_update_lastmovies/<str:pk>/',admin_update_lastmovies,name='admin_update_lastmovies'),
    path('admin_delete_lastmovies/<str:pk>/',admin_delete_lastmovies,name='admin_delete_lastmovies'),
    #movies urls
    path('admin_create_movies/',admin_create_movies,name='admin_create_movies'),
    path('admin_views_movies/<str:pk>/',admin_views_movies,name='admin_views_movies'),
    path('admin_update_movies/<str:pk>/',admin_update_movies,name='admin_update_movies'),
    path('admin_delete_movies/<str:pk>/',admin_delete_movies,name='admin_delete_movies'),
    #movies urls
    #login urls
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('sing_up_user',sing_up_user,name='sing_up_user')

]
