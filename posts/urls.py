from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),

    path("post/new/", PostCreateView.as_view(), name="post-create"),

    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),

    path("post/<slug:slug>/edit/", PostUpdateView.as_view(), name="post-update"),

    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post-delete"),
]            