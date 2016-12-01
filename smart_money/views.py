from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from smart_money.models import Company
# Create your views here.
def index(request):
    companies_byname= Company.objects.all().order_by('-name')
    index_page = loader.get_template('smart_money/index.html')
    return HttpResponse(index_page.render())

def team(request):
    team_page = loader.get_template('smart_money/team.html')
    return HttpResponse(team_page.render())

def funding(request):
    funding_page = loader.get_template('smart_money/funding.html')
    return HttpResponse(funding_page.render())

def market(request):
    market_page = loader.get_template('smart_money/market.html')
    return HttpResponse(market_page.render())

def postition(request):
    position_page = loader.get_template('smart_money/postition.html')
    return HttpResponse(position_page.render())

def awareness(request):
    awareness_page = loader.get_template('smart_money/awareness.html')
    return HttpResponse(awareness_page.render())

def position(request):
    position_page = loader.get_template('smart_money/position.html')
    return HttpResponse(position_page.render())
