from django import forms
from django.db import connections
from crispy_forms.helper import FormHelper

def establishments():
    with connections['ecourtisuserdb'].cursor() as cursor:
        cursor.execute("select est_dbname, estname from establishment")
        result = cursor.fetchall()
        establishments = [('', 'Select Establishment')]
        return establishments + result


class LoginForm(forms.Form):
    establishment = forms.ChoiceField(choices=establishments())
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False 