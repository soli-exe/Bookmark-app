from .models import BookMark
from bootstrap_modal_forms.forms import BSModalModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class BookmarkModelForm(BSModalModelForm):
    class Meta:
        model = BookMark
        exclude = ['timestamp']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
