from django.urls import path, include
from rest_framework import routers
from .import views

urlpatterns = [
    path('login/', views.user_login, name='login'),

    path('get-users/', views.get_users, name='get-users'),

    path('create-user/', views.create_user, name='create-user'),

    path('user/update-user-details/<int:id>', views.update_user_details, name='update-user'),
    path('user/change-password/<int:id>', views.change_password, name='change-password'),
    path('user/delete/<int:id>', views.delete_user, name='delete-user'),
]
