from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls.base import reverse_lazy
from accounts.forms import Registration
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


class SignUpView(BSModalCreateView):
    form_class = Registration
    template_name = 'signup.html'
    success_message = 'Sign up succeeded.'
    success_url = reverse_lazy('index')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {
        'form': form
    })
