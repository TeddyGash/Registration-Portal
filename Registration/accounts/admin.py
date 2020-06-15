from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm, CustomUserChangeForm
from portalapp.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'first_name', 'last_name', 'middle_name', 'gender', 'rotation']

admin.site.register(User, CustomUserAdmin)