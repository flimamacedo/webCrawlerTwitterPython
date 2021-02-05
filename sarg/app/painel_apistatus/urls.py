from django.urls import path

from . import views

urlpatterns = [
    path('endpoints', views.ShowEndpoints),
    path('tweets', views.ShowTweets),    
    path('apistatus', views.ShowApiStatus),
]
