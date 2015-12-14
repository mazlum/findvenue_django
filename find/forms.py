#-*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.models import ModelForm
from find.models import UserKey

ERROR_MESSAGES = {
    'required': "Bu alan zorunludur.",
    'invalid': "Geçersiz değer."
}

class RegistrationForm(UserCreationForm):
    username = CharField(error_messages=ERROR_MESSAGES)
    password1 = CharField(error_messages=ERROR_MESSAGES)
    password2 = CharField(error_messages=ERROR_MESSAGES)
    first_name = CharField(error_messages=ERROR_MESSAGES)
    email = CharField(error_messages=ERROR_MESSAGES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not len(password) > 5:
            raise ValidationError("Şifre en az 6 karakter olmalıdır.")
        return password



class LoginForm(AuthenticationForm):
    username = CharField(error_messages=ERROR_MESSAGES)
    password = CharField(error_messages=ERROR_MESSAGES)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_messages = {
            'invalid_login': "Geçersiz kullanıcı adı, şifre.",
            'inactive': "Hesap inaktif.",
        }


class KeyControlForm(ModelForm):
    class Meta:
        model = UserKey
        fields = ['key']