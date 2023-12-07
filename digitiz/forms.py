from django import forms

from core.models import CaseType, DocumentType



class IndexRegisterSearchForm(forms.Form):

    case_type   = forms.ModelChoiceField(
                        label='',
                        queryset=CaseType.objects.using('chnccc').filter(display='Y').order_by('type_name'),
                    )
    case_number = forms.CharField(
                        label='',
                        widget=forms.TextInput(attrs={'placeholder' : "Case Number"})
                    )
    case_year   = forms.CharField(
                        label='',
                        widget=forms.TextInput(attrs={'placeholder' : "Case Year"})
                    )

    def __init__(self, *args, **kwargs):
        super(IndexRegisterSearchForm, self).__init__(*args, **kwargs)
        self.fields['case_type'].empty_label = "    Select casetype"



class IndexRegisterForm(forms.Form):
    serial_number   = forms.CharField(required=False)
    description     = forms.ModelChoiceField(queryset=DocumentType.objects.using('chnccc').filter(display='Y'))
    document_date   = forms.DateField(required=False)
    no_of_parts     = forms.CharField(required=False)
    document        = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super(IndexRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['case_type'].empty_label = "Select casetype"