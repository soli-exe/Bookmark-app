from .models import CustomUser
from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin, PopRequestMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Registration(PopRequestMixin, CreateUpdateAjaxMixin,
                   UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['phone'].required = False

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
