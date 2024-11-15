from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import CustomUser
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@csrf_exempt
def user_login(request):
    try:
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                return JsonResponse({'ok': False, 'msg': '账号或密码错误1'})
            if not CustomUser.objects.filter(username=username).exists():
                return JsonResponse({'ok': False, 'msg': '账号或密码错误2'})
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'ok': True, 'msg': '登录成功,即将跳转到首页'})
            else:
                return JsonResponse({'ok': False, 'msg': '账号或密码错误3'})
    except Exception as e:
        return JsonResponse({'ok': False, 'msg': '服务器错误，请稍后再试。'}, status=500)


def user_logout(request):
    logout(request)
    return JsonResponse({'ok': True, 'msg': '退出成功'})


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'ok': False, 'msg': '账号已存在'})
        if not username or not password:
            return JsonResponse({'ok': False, 'msg': '账号或密码错误'})
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'ok': False, 'msg': '账号已存在'})
        CustomUser.objects.create_user(username=username, password=password)
        return JsonResponse({'ok': True, 'msg': '注册成功,即将跳转到登录页'})
