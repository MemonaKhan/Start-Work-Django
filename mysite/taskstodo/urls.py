from django.urls import path
from . import views
# app_name = "tasks"          # and use it by using tasks:index in url in a tag like {% url 'tasks:index' %}
urlpatterns = [
    path("", views.index, name="viewtasks"),   
    path("add", views.add, name="add"),   

]