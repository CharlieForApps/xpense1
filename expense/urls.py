
from django.conf.urls import url

from .views import (
	ExpenseCreateView,
	ExpenseListView,
	ExpenseUpdateView,	
	ExpenseDeleteView,	
)

urlpatterns = [    
    url(r'^$', ExpenseListView.as_view(), name='list'),
    url(r'^create/$', ExpenseCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', ExpenseUpdateView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', ExpenseDeleteView.as_view(), name='delete'),
]
