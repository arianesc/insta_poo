from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

'''
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=255, label=_("Nome"), required=False)
    last_name = forms.CharField(max_length=255, label=_("Sobrenome"), required=False)
    country = forms.CharField(max_length=255, label=_("País"), required=False)
    state = forms.CharField(max_length=255, label=_("Estado"), required=False)
    city = forms.CharField(max_length=255, label=_("Cidade"), required=False)
    company = forms.CharField(max_length=255, label=_("Empresa"), required=False)
    birth_date = forms.DateField(label=_("Data de Nascimento"), required=False)
    marital_status = forms.ChoiceField(
        choices=User.MARITAL_STATUS_CHOICES, label=_("Estado Civil"), required=False
    )'''


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input login', 'type':'text', 'id':'Valido', 'name':'Valido',
         'required':'required', 'placeholder':'username',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'input login', 'type':'password', 'name':'senha',
                                     'required':'required', 'placeholder':'Senha'}))

