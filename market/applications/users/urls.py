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
        'users/register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'users/logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'users/update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),
        name='user-update_password',
    ),
    path(
        'users/update/<pk>/', 
        views.UserUpdateView.as_view(),
        name='user-update',
    ),
    path(
        'users/delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
    path(
        'users/lista/', 
        views.UserListView.as_view(),
        name='user-lista',
    ),
]