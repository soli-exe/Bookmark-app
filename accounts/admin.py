from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, Registration
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = Registration
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
