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

from eauth.forms import LoginForm
from eauth.models import Users


def get_establishment(establishment):
    with connections['ecourtisuserdb'].cursor() as cursor:
        cursor.execute("select est_code from establishment where est_dbname= %s ", [establishment])
        return cursor.fetchone()
    

def verify_user_role(user, establishment):
    with connections['ecourtisuserdb'].cursor() as cursor:
        cursor.execute("select establishmentid, user_id, court_id from id_role_est where user_id= %s and establishmentid= %s and court_id is not null", [user, establishment])
        result = cursor.fetchone()
        return result

 
def login(request):

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
                User.objects.get(username=username)
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
