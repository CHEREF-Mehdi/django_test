from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.models import User


class Register(View):
    context = {
        'title': 'Ayomi User Registration',
        'form': UserRegistrationForm()
    }

    def get(self, request):
        return render(request, 'user/register.html', self.context)

    def post(self, request):
        self.context['form'] = UserRegistrationForm(request.POST)

        if self.context['form'].is_valid():
            self.context['form'].save()
            username = self.context['form'].cleaned_data.get('username')
            messages.success(
                request, f'Account created successfuly for {username}')
            return redirect('user-login')

        return render(request, 'user/register.html', self.context)


class Home(View):
    context = {'title': 'Ayomi Home'}

    @method_decorator(login_required)
    def get(self, request):
        self.context['form'] = UserUpdateForm(instance=request.user)
        return render(request, 'user/home.html', self.context)

    @method_decorator(login_required)
    def post(self, request):
        self.context['form'] = UserUpdateForm(
            request.POST, instance=request.user)

        if self.context['form'].has_changed():
            if self.context['form'].is_valid():
                newEmail = self.context['form'].cleaned_data.get('email')

                count = User.objects.filter(
                    email=newEmail).exclude(
                    username=request.user.username).count()

                if count > 0:
                    data = {'message': 'Form validation errors.',
                            'type': 'danger',
                            'error': {'email': [{'message': 'Email already exists.', 'code': ''}]}
                            }
                else:
                    self.context['form'].save()
                    data = {'message': 'Your account has been updated',
                            'type': "success",
                            'user': self.context['form'].cleaned_data
                            }
            else:
                errors = {f: e.get_json_data()
                          for f, e in self.context['form'].errors.items()}
                data = {'message': 'Form validation errors.',
                        'type': 'danger',
                        'error': errors
                        }
        else:
            data = {'message': 'no updates', 'type': 'none'}

        return JsonResponse(data)
