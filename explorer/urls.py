from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #starts with post/pk/end
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
