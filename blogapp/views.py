from django.shortcuts import render
from django.views.generic import FormView

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
