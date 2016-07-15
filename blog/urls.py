from django.conf.urls import url
from blog import views


urlpatterns = [

    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/new/$', views.post_new, name='post_new'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),


	]
