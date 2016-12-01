from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from smart_money.models import Company
# Create your views here.
def index(request):
    companies_byname= Company.objects.all().order_by('-name')
    x = loader.get_template('smart_money/index.html')
    c = Context({'companies_byname':companies_byname, })
    return HttpResponse(x.render())
