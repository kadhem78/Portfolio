from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('project/<slug:slug>' , views.project_detail , name="project_detail"),
]


htmxurlpatterns = [
    path('add_message' , views.create_message , name="create_message"),
]

urlpatterns += htmxurlpatterns