
from django.conf.urls import url

from .views import (
	CategoryCreateView,
	CategoryListView,
	CategoryUpdateView,	
	CategoryDeleteView,	
	# CategoryDetailView,
)

urlpatterns = [    
    url(r'^$', CategoryListView.as_view(), name='list'),
    url(r'^create/$', CategoryCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', CategoryUpdateView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', CategoryDeleteView.as_view(), name='delete'),
    # url(r'^lists/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='details'),
    
]
