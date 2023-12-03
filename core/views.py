from django.db import connections
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.models import CivilPending, DailyProceeding, CaseTypePending, HearingStatus, Designation
from digitiz import forms


from core.utils import *


@login_required
def dasboard(request):
    context = {
        'listed_today': case_listed_today(),
        'registered_today': registered_today(),
        'unregistered_today': unregistered_today(),
        'registered_groupby': registered_groupby(),
        'unregistered_groupby': unregistered_groupby(),
        'undated_cases': undated_cases(),
        'area': case_count(),
        'area_type': case_count_type()
    }
    return render(request, "core/dashboard.html", context)


def case_list(request):
    case_list = HearingStatus.objects.using('chnccc').filter(hearing_date='2023-11-16').filter(court_no=1).filter(cino__regcase_type__isnull=False).order_by('cino__purpose_today__purpose_name')
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
    return render(request, "core/case_list.html", context)


def undated_list(request):
    case_list = CivilPending.objects.using('chnccc').filter(date_of_decision__isnull=True).filter(court_no=1).filter(date_next_list__lte='2023-12-03')
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
    return render(request, "core/undated_list.html", context)



def case_details(request, caseno):
    context = {
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno)
    }
    return render(request, "core/case_details.html", context)


def view_bdiary(request, caseno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno),
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'diaries': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    }
    return render(request, "core/view_bdiary.html", context)


def view_oldbdiary(request, caseno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno),
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'diaries': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    }
    return render(request, "core/view_oldbdiary.html", context)



def view_diary(request, caseno, srno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno), 
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),      
        'diary': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(srno=srno).first()
    }
    return render(request, "core/view_olddiary.html", context)


def view_odiary(request, caseno, srno):
    context = {
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno), 
        'diary': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(srno=srno).first()
    }
    return render(request, "core/view_olddiary.html", context)


def order_sheet(request):
    context = {
        'form': forms.IndexSearchForm(),
    }
    if request.method == 'POST':
        # initial = {
        #     'case_type' : request.POST.get('case_type'),
        #     'case_number': request.POST.get('case_number'),
        #     'case_year': request.POST.get('case_year')
        # }
        context['search'] = True
        form = forms.IndexSearchForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            case_year = form.cleaned_data['case_year']
            context['case'] = CivilPending.objects.using('chnccc').filter(regcase_type=case_type).filter(reg_no=case_number).filter(reg_year=case_year).first()
            # context['designation'] = Designation.objects.using('chnncc').filter(courtno=1).first()

    return render(request, "core/order_sheet.html", context)