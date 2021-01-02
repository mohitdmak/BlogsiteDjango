from django.urls import path
from .import views
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns=[
    path("",PostListView.as_view() , name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view() ,name="post_detail"),
    path("post/new/",PostCreateView.as_view(), name="post-create"),
    path("about/",views.about, name="BLOG-ABOUT"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="update_post"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(),name="delete_post")
]