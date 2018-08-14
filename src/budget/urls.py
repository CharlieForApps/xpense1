
from django.conf.urls import url

from .views import (
	BudgetCreateView,
	BudgetListView,
	BudgetUpdateView,	
	BudgetDeleteView,	
)

urlpatterns = [    
    url(r'^$', BudgetListView.as_view(), name='list'),
    url(r'^create/$', BudgetCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', BudgetUpdateView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', BudgetDeleteView.as_view(), name='delete'),
]
