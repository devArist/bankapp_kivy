from django.urls import path
from api import apiviews

urlpatterns = [
    path('blog', apiviews.blogs, name='blogs'),
    path('blog/<int:pk>', apiviews.blog, name='blog')
]
