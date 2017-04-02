from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.leg_list, name='leg_list'),
]