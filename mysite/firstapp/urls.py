from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),             # "" means no additional route, nothing at end of url
    path("name", views.name, name="name"),             
    # path("<str:name>", views.greet, name="greet"),             
    path("home", views.home, name="home"),   
    path("<str:name>", views.page, name="page"),             

]