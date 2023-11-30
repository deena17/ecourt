from django.db import connections
from django.shortcuts import render
from django.urls import reverse

from core.models import CaseTypePending, IndexRegister, CivilPending
from digitiz.forms import IndexSearchForm, IndexForm


def casetypes():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select type_code, case_type from case_type_t where display='Y' order by type_name ASC")
        result = cursor.fetchall()
        data = [('', 'Select Casetype')]
        return data + result

def list_index(request):
    context = {
        'form' : IndexSearchForm(),
        'search': False,
        'casetypes' : CaseTypePending.objects.using('chnccc').filter(display='Y').order_by('type_name'),
    }
    if request.method == 'POST':
        context['search'] = True
        form = IndexSearchForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            case_year = form.cleaned_data['case_year']
            data = CivilPending.objects.using('chnccc').filter(regcase_type=case_type).filter(reg_no=case_number).filter(reg_year=case_year).first()
            if data:
                context['documents'] = IndexRegister.objects.using('chnccc').filter(display='Y').filter(caseno=data.case_no).order_by('-paperdate')
    return render(request, "digitiz/list_index.html", context)


def add_documents(request):
    context = {
        'form' : IndexForm(),
        'search': False,
        'casetypes' : CaseTypePending.objects.using('chnccc').filter(display='Y').order_by('type_name'),
    }
    return render(request, "digitiz/list_index.html", context)
