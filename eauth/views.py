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


def login_create(request):
    """ authenticate the user with credentials if exists or create a newuser """
    context = {}
    # user = None
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
            password_hash   = hashlib.md5(password.encode('utf-8')).hexdigest()
            est_code        = get_establishment(establishment)
            try:
                # check if the user exists in the djanog authentication system
                user = User.objects.filter(username=username).first()
                if user and user.is_superuser:
                    authendicated = authenticate(username=username, password=password)
                    if authendicated:
                        auth_login(request, user)
                        if 'next_url' in request.session:
                            return HttpResponseRedirect(request.session['next_url'])
                        else:
                            return HttpResponseRedirect(reverse('dashboard'))
                ecourt_user = get_user(username)
                if user:
                    role = verify_user_role(ecourt_user.userid, est_code)
                    if not role:
                        messages.error(request, 'User role not defined. Please contact the system administrator')
                        return HttpResponseRedirect(reverse('login'))
                    authendicated = authenticate(username=username, password=password)
                    if not authendicated:
                        messages.error(request, 'Invalid username or password')
                        return HttpResponseRedirect(reverse('login'))
                    if authendicated:
                        if authendicated.is_active:
                            auth_login(request, user)
                            request.session['establishment'] = establishment
                            if 'next_url' in request.session:
                                return HttpResponseRedirect(request.session['next_url'])
                            else:
                                return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        messages.warning(request, 'Your account is not active, Please contact the admin')
                        return HttpResponseRedirect(reverse('login'))
            except User.DoesNotExist:
                pass
            else:
                # create a new user in the django authentication system
                user = Users.objects.using('ecourtisuserdb').filter(username=username).filter(user_password=password_hash).first()
                if not user:
                    messages.error(request, 'Invalid username or password')
                    return HttpResponseRedirect(reverse('login'))
                else:
                    role = verify_user_role(user.userid, est_code)
                    if not role:
                        messages.error(request, 'User role not defined. Please contact the system administrator')
                        return HttpResponseRedirect(reverse('login'))
                    else:
                        user = User.objects.create(username=username, first_name=username,last_name=username,password=make_password(password),is_active=True,is_staff=True)
                        user.save()
                        authendicated = authenticate(username=user.username, password=user.password)
                        auth_login(request, user)
                        return HttpResponseRedirect(reverse('dashboard'))
            finally:
                # create a profile if not exists for the user
                request.session['establishment'] = establishment 
                if user:
                    profile = Profile.objects.filter(user=user).first()
                    profile.establishment_code=est_code 
                    profile.court_no=role[2]
                    profile.save()  
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
    return HttpResponseRedirect(reverse('login'))
    # form=LoginForm()
    # return render(request, 'eauth/login.html', {'form':form})





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



    # def login_create(request):
    # """ authenticate the user with credentials if exists or create a newuser """
    # context = {}
    # context['form'] = LoginForm()
    # next_url = request.GET.get('next')
    # if next_url:
    #     request.session['next_url'] = next_url
    # if request.user.is_authenticated:
    #     if 'next_url' in request.session:
    #         return HttpResponseRedirect(request.session['next_url'])
    # if request.method == 'POST':
    #     form=LoginForm(request.POST)
    #     if form.is_valid():
    #         establishment   = form.cleaned_data["establishment"]
    #         username        = form.cleaned_data['username']
    #         password        = form.cleaned_data['password']
    #         password_hash   = hashlib.md5(password.encode('utf-8')).hexdigest()
    #         est_code        = get_establishment(establishment)
    #         try:
    #             # verify if user exists in django auth then authenticate
    #             user = User.objects.filter(username=username).first()
    #             if user and user.is_superuser:
    #                 authendicated = authenticate(username=username, password=password)
    #                 if authendicated:
    #                     request.session['establishment'] = establishment
    #                     auth_login(request, user)
    #                     if 'next_url' in request.session:
    #                         return HttpResponseRedirect(request.session['next_url'])
    #                     else:
    #                         return HttpResponseRedirect(reverse('dashboard'))
    #             ecourt_user = get_user(username)
    #             if user:
    #                 role = verify_user_role(ecourt_user.userid, est_code)
    #                 if not role:
    #                     messages.error(request, 'User role not defined. Please contact the system administrator')
    #                     return HttpResponseRedirect(reverse('login'))
    #                 profile = Profile.objects.filter(user=user).first()
    #                 profile.establishment_code=est_code 
    #                 profile.court_no=role[2]
    #                 profile.save()
    #                 authendicated = authenticate(username=username, password=password)
    #                 if not authendicated:
    #                     messages.error(request, 'Invalid username or password')
    #                     return HttpResponseRedirect(reverse('login'))
    #                 if authendicated:
    #                     if authendicated.is_active:
    #                         auth_login(request, user)
    #                         request.session['establishment'] = establishment
    #                         if 'next_url' in request.session:
    #                             return HttpResponseRedirect(request.session['next_url'])
    #                         else:
    #                             return HttpResponseRedirect(reverse('dashboard'))
    #                 else:
    #                     messages.warning(request, 'Your account is not active, Please contact the admin')
    #                     return render(request, 'core/common/login.html', {'form':form})
    #             else:
    #                 user = Users.objects.using('ecourtisuserdb').filter(username=username).filter(user_password=password_hash).first()
    #                 if not user:
    #                     messages.error(request, 'Invalid username or password')
    #                     return HttpResponseRedirect(reverse('login'))
    #                 else:
    #                     role = verify_user_role(user.userid, est_code)
    #                     if not role:
    #                         messages.error(request, 'User role not defined. Please contact the system administrator')
    #                         return HttpResponseRedirect(reverse('login'))
    #                     else:
    #                         user = User.objects.create(username=username, first_name=username,last_name=username,password=make_password(password),is_active=True,is_staff=True)
    #                         user.save()
    #                         profile = Profile.objects.filter(user=user).first()
    #                         profile.establishment_code=est_code
    #                         profile.court_no=role[2]
    #                         authendicated = authenticate(username=user.username, password=user.password)
    #                         auth_login(request, user)
    #                         request.session['establishment'] = establishment
    #                         return HttpResponseRedirect(reverse('dashboard'))
    #         except User.DoesNotExist:
    #             pass      
    # return render(request, "eauth/login.html", context)