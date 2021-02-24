from .models import CustomUser
from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin, PopRequestMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Registration(PopRequestMixin, CreateUpdateAjaxMixin,
                   UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
