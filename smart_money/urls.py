from django.conf.urls import url
from smart_money import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^team/',views.team, name='team'),
    url(r'^awareness/',views.awareness, name='awareness'),
    url(r'^funding/',views.funding, name='funding'),
    url(r'^position/',views.position, name='position'),
    url(r'^market/',views.market, name='market'),

]
