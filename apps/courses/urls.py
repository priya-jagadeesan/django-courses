from django.conf.urls import url,include
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/destroyID/(?P<id>\d+)$', views.destroyId),
    url(r'^courses/comment/(?P<id>\d+)/show$', views.comments),
    url(r'^courses/comment/(?P<id>\d+)/add$', views.addComment),
]
