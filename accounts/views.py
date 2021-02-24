from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls.base import reverse_lazy
from accounts.forms import Registration


class SignUpView(BSModalCreateView):
    form_class = Registration
    template_name = 'signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')
