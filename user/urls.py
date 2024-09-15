from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.userlogin, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("add_profile/", views.add_profile, name="add_profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("delete_profile/", views.delete_profile, name="delete_profile"),
]
