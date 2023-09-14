
from django.urls import path
from .views import project_detail, project_index

urlpatterns = [
    path("", project_index, name= "project_index"),
    path("<int:id>/", project_detail, name= "project_detail"),
]
