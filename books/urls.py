from django.conf.urls import url, include
from django.views.generic import TemplateView

from books import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.book_list, name='book_list'),
    url(r'^create/$', views.book_create, name='book_create'),
    url(r'^(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]
