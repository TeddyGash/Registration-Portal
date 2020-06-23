from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('accounts:register_success')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})


class LoginView(FormView):
    success_url = 'portalapp:home'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'accounts/login.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(FormView):
    url = 'portalapp:home'
    template_name = 'portalapp/home2.html'

    def get(self, request):
        auth_logout(request)
        return super(LogoutView, self).get(request)

# @login_required
class DashboardView(LoginRequiredMixin, TemplateView):
    model = User
    context_object_name = 'user'
    template_name = "accounts/dashboard.html"


# def dashboard(request):
#     url = 'accounts:dashboard'
#     template_name = 'accounts/dashboard.html'
#     reg_list= User.objects.all()