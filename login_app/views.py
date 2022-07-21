from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from login_app import forms
from login_app.models import User, UserCity


def home(request):
    return render(request, 'login_app/home.html')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method =='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            otp = form.cleaned_data['otp']
            try:
                user = User.objects.get(phone=phone, otp=otp)
                if user is not None and user.is_staff == False:
                    login(request,user)
                    message = f'Hello {user.phone} !'
                    return redirect('home/')
                elif user.is_staff:
                    login(request,user)
                    return redirect('admin/')
                else:
                    message  = 'Login faild'
            except Exception:
                message = f'phone/otp not match'

    return render(request, 'login_app/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


class UserCity(ListView):
    template_name = 'login_app/city.html'
    model = UserCity
    queryset = UserCity.objects.values('city__city').annotate(ucount=Count('user')) 




