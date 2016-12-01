from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from smart_money.models import Company
# Create your views here.
def index(request):
    return HttpResponse(loader.get_template('smart_money/index.html'))
