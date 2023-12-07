from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from core.models import CaseType, IndexRegister, Civil
from digitiz.forms import IndexRegisterSearchForm, IndexRegisterForm


def list_index(request):
    context = {
        'form' : IndexRegisterSearchForm(),
        'search': False,
        'casetypes' : CaseType.objects.using('chnccc').filter(display='Y').order_by('type_name'),
    }
    if request.method == 'POST':
        # initial = {
        #     'case_type' : request.POST.get('case_type'),
        #     'case_number': request.POST.get('case_number'),
        #     'case_year': request.POST.get('case_year')
        # }
        context['search'] = True
        form = IndexRegisterSearchForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            case_year = form.cleaned_data['case_year']
            data = Civil.objects.using('chnccc').filter(regcase_type=case_type).filter(reg_no=case_number).filter(reg_year=case_year).first()
            if data:
                context['documents'] = IndexRegister.objects.using('chnccc').filter(display='Y').filter(caseno='232100003362016').order_by('-paperdate')
    return render(request, "digitiz/list_index.html", context)


def add_documents(request, caseno=None):
    establishment = request.session['establishment']
    context = {}
    if caseno is not None:
        try: 
            Civil.objects.using(establishment).get(case_no=caseno)
        except Civil.DoesNotExist:
            messages.warning(request, "Case doesn't exists or not belongs to this court ")
            return HttpResponseRedirect(reverse('add-document'))
    context['search_form']   = IndexRegisterSearchForm()
    context['register_form'] = IndexRegisterForm() 
    context['casetypes'] = CaseType.objects.using('chnccc').filter(display='Y').order_by('type_name')
    context['submitted'] = False
    if request.method == 'POST':
        search_form   = IndexRegisterSearchForm(request.POST)
        register_form = IndexRegisterForm(request.POST)
        if search_form.is_valid():
            case_type     = search_form.cleaned_data['case_type']
            case_number   = search_form.cleaned_data['case_number']
            case_year     = search_form.cleaned_data['case_year']
            case  = Civil.objects.using(establishment).filter(regcase_type=case_type).filter(reg_no=case_number).filter(reg_year=case_year).first()
            if not case:
                messages.warning(request, "Case doesn't exist or not belongs to this court")
                return HttpResponseRedirect(reverse('add-document'))
            context['submitted'] = True
        if register_form.is_valid():
            description      = register_form.cleaned_data['description']
            print(description)


    return render(request, "digitiz/add_index.html", context)
