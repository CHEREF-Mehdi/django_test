from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Register(View):
    context = {
        'title': 'Ayoumi User Registration',
        'form': UserRegistrationForm()
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'user/register.html', self.context)

    def post(self, request, *args, **kwargs):
        self.context['form'] = UserRegistrationForm(request.POST)

        if self.context['form'].is_valid():
            self.context['form'].save()
            username = self.context['form'].cleaned_data.get('username')
            messages.success(
                request, f'Account created successfuly for {username}')
        return render(request, 'user/register.html', self.context)


class Login(View):
    context = {
        'title': 'Ayoumi user Login'
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html', self.context)


class Home(View):
    context = {
        'title': 'Ayoumi Home'
    }

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, 'user/home.html', self.context)
