from django.conf.urls import url

from .views import (
	PeriodCreateView,
	PeriodListView,
	PeriodUpdateView,	
	PeriodDeleteView,	
)
# app_name = 'period'
urlpatterns = [    
    url(r'^$', PeriodListView.as_view(), name='list'),
    url(r'^create/$', PeriodCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', PeriodUpdateView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', PeriodDeleteView.as_view(), name='delete'),

    
]
