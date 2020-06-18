from django.urls import path
from git_class import views

urlpatterns = [
    path('', views.git_tutorials, name='git_tutorials')
]