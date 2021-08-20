from django.urls import path
from . import views
from tarix import views as vw


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tarix/', vw.emrooz, name='emrooz'),
]