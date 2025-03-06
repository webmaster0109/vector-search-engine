from django.urls import path
from .views import vector_search_home

urlpatterns = [
    path("", vector_search_home, name="vector_search_home"),
]
