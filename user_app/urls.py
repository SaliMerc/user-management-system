from django.urls import path
from .import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),

    path('api/get-users/', views.get_users, name='get-users'),

    path('api/create-user/', views.create_user, name='create-user'),

    path('api/user/update-user-details/<int:id>', views.update_user_details, name='update-user'),
    path('api/user/change-password/<int:id>', views.change_password, name='change-password'),
    path('api/user/delete/<int:id>', views.delete_user, name='delete-user'),
]
