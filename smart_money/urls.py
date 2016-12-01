from django.conf.urls import url
from smart_money import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
