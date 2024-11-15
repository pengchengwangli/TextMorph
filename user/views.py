from django.shortcuts import render
from user.models import CustomUser
# Create your views here.

def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')