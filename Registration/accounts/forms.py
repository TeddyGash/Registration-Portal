from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from portalapp.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# class SignUpForm(UserCreationForm):
# 	first_name = forms.CharField(max_length=30, required=True, help_text='Required.'),
# 	middle_name = forms.CharField(max_length=30, required=False, help_text='Optional.'),
# 	last_name = forms.CharField(max_length=30, required=True, help_text='Required.'),
#     gender = forms.CharField(max_length=10, required=True, help_text='Required.'),
#     rotation = forms.CharField(max_length=30, required=True, help_text='Required.')
   
#     class Meta:
#         model = User
#         fields = ('first_name', 'middle_name', 'last_name', 'gender', 'rotation', 'password1', 'password2')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required..')
    middle_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    gender = forms.CharField(max_length=10, required=True, help_text='Required.')
    rotation = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'gender', 'rotation', 'email', 'password1', 'password2')
    

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required..')
    middle_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    gender = forms.CharField(max_length=10, required=True, help_text='Required.')
    rotation = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'gender', 'rotation', 'email')