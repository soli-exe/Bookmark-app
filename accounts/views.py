from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls.base import reverse_lazy
from accounts.forms import Registration


class SignUpView(BSModalCreateView):
    form_class = Registration
    template_name = 'signup.html'
    success_message = 'Sign up succeeded.'
    success_url = reverse_lazy('index')
