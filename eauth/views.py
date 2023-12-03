import hashlib

from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from eauth.forms import LoginForm
from eauth.models import Users, Profile
from eauth.utils import *


"""
    if user exists in django auth
        verify with the credentials and authenticate
        if not verified 
            check the password with ecourtisuserdb and update in django auth and authenticate
    else 
        verfiy the credentials with ecourtisuserdb
        if verified create the new user in django
        else throw an error message
"""
 
def login_create(request):
    """ authenticate the user with credentials if exists or create a newuser """
    context = {}
    context['form'] = LoginForm()
    next_url = request.GET.get('next')
    if next_url:
        request.session['next_url'] = next_url
    if request.user.is_authenticated:
        if 'next_url' in request.session:
            return HttpResponseRedirect(request.session['next_url'])
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            establishment   = form.cleaned_data["establishment"]
            username        = form.cleaned_data['username']
            password        = form.cleaned_data['password']
            password        = form.cleaned_data["password"]
            password_hash   = hashlib.md5(password.encode('utf-8')).hexdigest()
            est_code        = get_establishment(establishment)
            try:
                auth = User.objects.get(username=username)
                Profile.objects.create(user=auth)
                user = authenticate(username=username, password=password)
                if not user:
                    messages.error(request, 'Invalid username or password')
                    return HttpResponseRedirect(reverse('login'))
                if user:
                    if user.is_active:
                        auth_login(request, user)
                        if 'next_url' in request.session:
                            return HttpResponseRedirect(request.session['next_url'])
                        else:
                            return HttpResponseRedirect('dashboard.index')
                    else:
                        messages.warning(request, 'Your account is not active, Please contact the admin')
                        return render(request, 'core/common/login.html', {'form':form})
            except User.DoesNotExist:
                pass
            else:
                user = Users.objects.using('ecourtisuserdb').filter(username=username).filter(user_password=password_hash)
                if not user:
                    messages.error(request, 'Invalid username or password')
                    return HttpResponseRedirect(reverse('login'))
                role = verify_user_role(user[0].userid, est_code[0])
                if not role:
                    messages.error(request, 'User role not defined. Please contact the system administrator')
                    return HttpResponseRedirect(reverse('login'))
            new_user = User.objects.create(
                username=username, 
                first_name=username,
                last_name=username,
                password=make_password(password),
                is_active=True,
                is_staff=True
                )
            new_user.save()
            new_user = authenticate(username=username, password=password)
            auth_login(request, new_user)
            request.session["userid"]        = user[0].userid
            request.session['establishment'] = establishment
            request.session['courtid']       = role[2]
            request.session['isLoggedIn']    = True
            return HttpResponseRedirect('dashboard.index')
    return render(request, "eauth/login.html", context)


@login_required
def change_password(request):
    pass
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change-password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'core/common/change_password.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully!!!.")
    form=LoginForm()
    return render(request, 'eauth/login.html', {'form':form})





    # context = {}
    # context['form'] = LoginForm()
    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         establishment = form.cleaned_data["establishment"]
    #         username      = form.cleaned_data["username"]
    #         password      = form.cleaned_data["password"]
    #         password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    #         est_code      = get_establishment(establishment)
    #         user = Users.objects.using('ecourtisuserdb').filter(username=username).filter(user_password=password_hash)
    #         if not user:
    #             messages.error(request, 'Invalid username or password')
    #             return HttpResponseRedirect(reverse('login'))
    #         role = verify_user_role(user[0].userid, est_code[0])
    #         if not role:
    #             messages.error(request, 'User role not defined. Please contact the system administrator')
    #             return HttpResponseRedirect(reverse('login'))
    #     request.session["userid"]        = user[0].userid
    #     request.session['establishment'] = establishment
    #     request.session['courtid']       = role[2]
    #     request.session['isLoggedIn']    = True
    #     return HttpResponseRedirect(reverse('dashboard.index'))
    # return render(request, 'eauth/login.html', context)