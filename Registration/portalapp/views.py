from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

def home(request):
    return render (request, 'portalapp/home2.html',
    {'title': 'HOME'
    })

# @login_required
class RegListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'list.html'

# def list(request):
#     users = User.objects.all()
#     return render (request, 'portalapp/list.html', {'title': 'list'
#     })


