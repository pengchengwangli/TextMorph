from django.urls import path, re_path
from user import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
]
app_name = 'user'