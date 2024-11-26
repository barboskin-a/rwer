from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import TemplateView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    return render(request, 'main/index.html')

class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'

def openpage(request, page):
    try:
        template = get_template(f'main/{page}.html')  # Исправлено: добавлено '/'
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, "Вы вошли в систему!")
                return redirect('main:home')  # Перенаправление после успешного входа
            else:
                messages.error(request, "Неверные учетные данные.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Убедитесь, что сохраняете хэш пароля
            user.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('main:login')  # или на страницу входа
    else:
        form = RegisterForm()  # Создание пустой формы

    return render(request, 'register.html', {'form': form})



class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'
