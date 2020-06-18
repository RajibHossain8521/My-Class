from django.urls import path
from home_page import views


urlpatterns = [
    path('', views.home_page_index, name='home_page_index'),
]