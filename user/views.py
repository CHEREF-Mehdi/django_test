from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

class Register(View):
    context = {
        'title': 'Ayoumi User Registration',
        'form': UserRegistrationForm()
    }

    def get(self, request):
        return render(request, 'user/register.html', self.context)

    def post(self, request):
        print(request.POST)
        self.context['form'] = UserRegistrationForm(request.POST)

        if self.context['form'].is_valid():
            self.context['form'].save()
            username = self.context['form'].cleaned_data.get('username')
            messages.success(
                request, f'Account created successfuly for {username}')
        return render(request, 'user/register.html', self.context)

class Home(View):
    context = {
        'title': 'Ayoumi Home'
    }

    @method_decorator(login_required)
    def get(self, request):
        self.context['form'] = UserUpdateForm(instance=request.user)
        return render(request, 'user/home.html', self.context)

    @method_decorator(login_required)
    def post(self, request):
        
        self.context['form'] = UserUpdateForm(request.POST,instance=request.user)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, 'Your account has been updated')
            data = {'result':'you made an update','user':self.context['form'].cleaned_data}
        else :
            data = data = {'result':'data not valid','user':''}
        
           
        return JsonResponse(data, safe=False)
