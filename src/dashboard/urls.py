
from django.conf.urls import url

from .views import (
	ExpenseAjaxViewBar,
    ExpenseAjaxViewPie,
    ExpenseAjaxViewBarBudget,
	# ExpenseListView,
	# ExpenseUpdateView,	
	# ExpenseDeleteView,	
)

from dashboard import views

urlpatterns = [
    url(r'^$', views.json_example, name='json_example'),
    url(r'^data/$', ExpenseAjaxViewBar.as_view(), name='dashboard_data'),
    url(r'^datapie/$', ExpenseAjaxViewPie.as_view(), name='dashboard_datapie'),
    url(r'^databar/$', ExpenseAjaxViewBarBudget.as_view(), name='dashboard_databar'),

]
