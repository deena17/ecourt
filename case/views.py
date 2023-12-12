from django.db import connections
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from core.models import Civil, DailyProceeding, CaseType, HearingStatus, Designation
from digitiz import forms

from core.utils import *


@login_required
def dasboard(request):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context = {
        'listed_today': case_listed_today(establishment, court_no),
        'registered_today': registered_today(establishment, court_no),
        'unregistered_today': unregistered_today(establishment, court_no),
        'registered_groupby': registered_groupby(establishment, court_no),
        'unregistered_groupby': unregistered_groupby(establishment, court_no),
        'undated_cases': undated_cases(establishment, court_no),
        'area': case_count(establishment, court_no),
        'area_type': case_count_type(establishment, court_no)
    }
    return render(request, "case/dashboard.html", context)


def case_list(request):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    if court_no:
        case_list = HearingStatus.objects.using(establishment).filter(hearing_date='2023-11-16').filter(court_no=court_no).filter(cino__regcase_type__isnull=False).order_by('cino__purpose_today__purpose_name')
    else:
        case_list = HearingStatus.objects.using(establishment).filter(hearing_date='2023-11-16').filter(cino__regcase_type__isnull=False).order_by('cino__purpose_today__purpose_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(case_list, 20)
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    context = {
        'cases' : cases
    }
    context = {
        'cases' : cases
    }
    return render(request, "case/case_list.html", context)


def registered_list(request):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    if court_no:
        case_list = HearingStatus.objects.using(establishment).filter(hearing_date='2023-11-16').filter(court_no=court_no).filter(cino__regcase_type__isnull=False).order_by('cino__purpose_today__purpose_name')
    else:
        case_list = HearingStatus.objects.using(establishment).filter(hearing_date='2023-11-16').filter(cino__regcase_type__isnull=False).order_by('cino__purpose_today__purpose_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(case_list, 20)
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    context = {
        'cases' : cases
    }
    context = {
        'cases' : cases
    }
    return render(request, "case/case_list.html", context)


def undated_list(request):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    if court_no:
        case_list = Civil.objects.using(establishment).filter(date_of_decision__isnull=True).filter(court_no=court_no).filter(date_next_list__lte='2023-12-03')
    else:
        case_list = Civil.objects.using(establishment).filter(date_of_decision__isnull=True).filter(date_next_list__lte='2023-12-03')
    page = request.GET.get('page', 1)
    paginator = Paginator(case_list, 20)
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    context = {
        'cases' : cases
    }
    return render(request, "case/undated_list.html", context)



def case_details(request, caseno):
    context = {}
    establishment = request.session['establishment']
    context['previous'] = DailyProceeding.objects.using(establishment).filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
    try:
        context['case'] = Civil.objects.using(establishment).get(case_no=caseno)
    except Civil.DoesNotExist:
        messages.error(request, 'Case details not found')
        return HttpResponseRedirect(reverse('listed-today'))
    return render(request, "case/case_details.html", context)


def view_bdiary(request, caseno):
    context = {}
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context['bgcolors'] = ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal']
    context['previous'] = DailyProceeding.objects.using(establishment).filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first()
    diaries_list  = DailyProceeding.objects.using(establishment).filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(diaries_list, 5)
    try:
        diaries = paginator.page(page)
    except PageNotAnInteger:
        diaries = paginator.page(1)
    except EmptyPage:
        diaries = paginator.page(paginator.num_pages)
    context['diaries'] = diaries
    try:
        context['case'] = Civil.objects.using(establishment).get(case_no=caseno)
    except Civil.DoesNotExist:
        messages.error(request, "Case details not found")
        return HttpResponseRedirect(reverse('listed-today'))
    return render(request, "case/view_bdiary.html", context)


def view_oldbdiary(request, caseno):
    context = {}
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context['bgcolors'] = ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
    context['previous'] = DailyProceeding.objects.using(establishment).filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
    context['diaries']  = DailyProceeding.objects.using(establishment).filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    try:
        context['case'] = Civil.objects.using(establishment).get(case_no=caseno),
    except Civil.DoesNotExist:
        messages.error(request, "Case details not found")
        return HttpResponseRedirect(reverse('listed-today'))
    return render(request, "case/view_oldbdiary.html", context)



def view_diary(request, caseno, srno):
    context = {}
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context['bgcolors'] = ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
    context['diary']  = DailyProceeding.objects.using(establishment).filter(case_no=caseno).filter(srno=srno).first()
    try:
        context['case'] = Civil.objects.using(establishment).get(case_no=caseno)
    except Civil.DoesNotExist:
        messages.error(request, "Case details not found")
        return HttpResponseRedirect(reverse('listed-today'))
    print(context)
    return render(request, "case/view_olddiary.html", context)


def view_odiary(request, caseno, srno):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context = {
        'case' : Civil.objects.using(establishment).get(case_no=caseno), 
        'diary': DailyProceeding.objects.using(establishment).filter(case_no=caseno).filter(srno=srno).first()
    }
    return render(request, "case/view_olddiary.html", context)


def order_sheet(request):
    establishment = request.session['establishment']
    court_no = request.user.profile.court_no
    context = {
        'form': forms.IndexRegisterSearchForm(),
    }
    if request.method == 'POST':
        # initial = {
        #     'case_type' : request.POST.get('case_type'),
        #     'case_number': request.POST.get('case_number'),
        #     'case_year': request.POST.get('case_year')
        # }
        context['search'] = True
        form = forms.IndexRegisterSearchForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            case_year = form.cleaned_data['case_year']
            context['case'] = Civil.objects.using(establishment).filter(regcase_type=case_type).filter(reg_no=case_number).filter(reg_year=case_year).filter(court_no=court_no).first()
            if not context['case']:
                messages.warning(request, 'Case does not exists or not belongs to this court')

    return render(request, "case/order_sheet.html", context)