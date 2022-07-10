from dictionary_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('find-world', views.find_world, name='find-world'),
]
