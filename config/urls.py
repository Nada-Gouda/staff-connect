from django.contrib import admin
from django.urls import path, include
from posts.views import PostListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PostListView.as_view(), name="home"),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
]