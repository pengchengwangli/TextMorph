from django.urls import path, re_path
from user import views

urlpatterns = [
    path('login/',views.user_login, name='user_login'),
    # path('register/', user.views.user_register, name='user_register'),
    # path('logout/', user.views.user_logout, name='user_logout'),
    # path('profile/', user.views.user_profile, name='user_profile'),
    # path('change_password/', user.views.change_password, name='change_password'),
    # path('change_avatar/', user.views.change_avatar, name='change_avatar'),
    # path('change_email/', user.views.change_email, name='change_email'),
    # path('change_phone/', user.views.change_phone, name='change_phone'),
    # path('change_nickname/', user.views.change_nickname, name='change_nickname'),
]

app_name = 'user'
