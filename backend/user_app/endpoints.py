from django.urls import path
from user_app.apis import RegisterUserAPI

urlpatterns = [
    path('add/', RegisterUserAPI.as_view(), name='add_user'),
    
]