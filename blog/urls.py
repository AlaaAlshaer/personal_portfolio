from django.urls import path
from blog.views import blog_category, blog_detail, blog_index

urlpatterns = [
    path("", blog_index, name= "blog_index"),
    path("<int:id>/", blog_detail, name= "blog_detail"),
    path("<str:category>/", blog_category, name= "blog_category"),
]
