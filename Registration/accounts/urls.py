from django.urls import path
from django.contrib.auth import views as dj_views
#from suit_dashboard.views import DashboardView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success/', dj_views.PasswordResetCompleteView.as_view(
				template_name='accounts/register_success.html'
				), name='register_success'),
    path('register/failed/', dj_views.PasswordResetCompleteView.as_view(
				template_name='accounts/register_failed.html'
				), name='register_failed'),
    path('login/', dj_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', dj_views.LogoutView.as_view(template_name='portalapp/home2.html'), name='logout'),
    path('dashboard/', views.DashboardView.as_view(template_name = "accounts/dashboard.html"), name='dashboard')
]