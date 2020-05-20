#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        '', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),
        name='user-update_password',
    ),
    path(
        'update/<pk>/', 
        views.UserUpdateView.as_view(),
        name='user-update',
    ),
    path(
        'delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
    path(
        'lista/', 
        views.UserListView.as_view(),
        name='user-lista',
    ),
]