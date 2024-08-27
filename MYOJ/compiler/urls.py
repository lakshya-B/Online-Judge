from django.urls import path
from compiler.views import submit, post

urlpatterns = [
    path("", submit, name='submit'),
    path("code/",post, name="post"),
]