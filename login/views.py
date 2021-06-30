from django.contrib import auth
from django.shortcuts import render, reverse, redirect

from login.forms import RegistrationForm, LoginForm
from news.models import history, News
from .models import MyUser

from django.contrib.auth import get_user_model
User = get_user_model()
# 处理注册功能
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()

            # 如果直接使用objects.create()方法后不需要使用save()
            return redirect(reverse("login:login"), {'all': all})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# 处理登录功能，渲染登录首页
def index_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                # 将username写入session，存入服务器
                auth.login(request, user)
                request.session['username'] = username
                # return redirect(reverse("index"), {'username':username, 'is':is_login})
                # return HttpResponseRedirect(reverse('index'))
                obj = redirect('index')
                return  obj

            else:
            # 登陆失败
                return render(request, 'login.html', {'form': form,'message': '密码错误，请重试！'})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# 用户退出
def logout(request):
        auth.logout(request)
        return redirect(reverse("index"))


# 获取用户信息及历史浏览
def user_view(request):
    user = request.user
    a = request.user.id
    b = history.objects.filter(user_id=a).order_by('-time')

    return render(request, 'history.html', { "b" : b , "a" : user})


