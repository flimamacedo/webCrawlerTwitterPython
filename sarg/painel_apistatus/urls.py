from django.urls import path

from . import views

urlpatterns = [
    path('endpoints', views.ShowEndpoints),
    path('apistatus', views.ShowApiStatus),
]
