from django import forms
from django_select2.forms import Select2Widget

from core.models import CaseType, DocumentType



class IndexSearchForm(forms.Form):

    case_type   = forms.ModelChoiceField(
                        label='',
                        queryset=CaseType.objects.using('chnccc').filter(display='Y').order_by('type_name'),
                        widget=forms.Select(attrs={'class': 'select2 select2-danger'}))
    case_number = forms.CharField(
                        label='',
                        widget=forms.TextInput(attrs={'placeholder' : "Case Number"})
                    )
    case_year   = forms.CharField(
                        label='',
                        max_length=4,
                        widget=forms.TextInput(attrs={'placeholder' : "Case Year"})
                    )

    def __init__(self, *args, **kwargs):
        super(IndexSearchForm, self).__init__(*args, **kwargs)
        self.fields['case_type'].empty_label = "    Select casetype"
        # self.fields['case_type'].



class IndexForm(forms.Form):
    case_type   = forms.ModelChoiceField(
                        label='',
                        queryset=CaseType.objects.using('chnccc').filter(display='Y').order_by('type_name'))
    case_number = forms.CharField(
                        label='',
                        widget=forms.TextInput(attrs={'placeholder' : "Case Number"})
                    )
    case_year   = forms.CharField(
                        label='',
                        max_length=4,
                        widget=forms.TextInput(attrs={'placeholder' : "Case Year"})
                    )
    serial_number = forms.CharField()
    description = forms.ModelChoiceField(queryset=DocumentType.objects.filter(display='Y'))
    document_date = forms.DateField()
    no_of_parts = forms.NumberInput()
    document = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        self.fields['case_type'].empty_label = "Select casetype"