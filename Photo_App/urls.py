from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("photo/<int:photo_id>/", views.photo_detail, name="photo_detail"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("register/", views.register, name="register"),
]
