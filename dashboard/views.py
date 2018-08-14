import json
from django.db.models import Count, Q, Sum
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from expense.models import Expense
from category.models import Category
from budget.models import Budget
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
import random
# from django.contrib.auth.models import User

from django.utils import timezone
import datetime

# Create your views here.

def json_example(request):
    return render(request, 'dashboard/json_example.html')

class ExpenseAjaxViewBar(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		data = {}
		days = 7
		start_date = timezone.now().today() - datetime.timedelta(days=30)
		# datetime_list = []
		labels = []
		salesItems = []
		backgroundColor = []

		dataset = Expense.objects \
			.filter(expensedate__gt=start_date) \
			.filter(user=self.request.user) \
			.values('expensedate') \
			.annotate(total_amount=Sum('amount')) \
			.order_by('expensedate')

		x=0
		for entry in dataset:
			labels.append(
					# new_time.strftime("%a")
					entry['expensedate']
				)	
			salesItems.append(
					# random.randint(13,13312)
					entry['total_amount']

				)
			backgroundColor.append(
					# "rgba(230, 66, 32, 1)"
					"rgba(255, 193, 7, 1)"
				)
			# x+=1		

		data['labels'] = labels
		data['data'] = salesItems	
		data['backgroundColor'] = backgroundColor

		return JsonResponse(data)


class ExpenseAjaxViewPie(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		data = {}
		days = 7
		start_date = timezone.now().today() - datetime.timedelta(days=30)

		labels = []
		salesItems = []
		backgroundColor = []
		
		dataset = Expense.objects \
			.filter(user=self.request.user) \
			.filter(expensedate__gt=start_date) \
			.values('category__name') \
			.annotate(total_amount=Sum('amount')) \
			.order_by('category__name')

		for entry in dataset:
			labels.append(
					entry['category__name']
				)	
			salesItems.append(
					entry['total_amount']

				)
			backgroundColor.append(
					"rgba(255, 193, 7, 1)"
				)	

		data['labels'] = labels
		data['data'] = salesItems	
		data['backgroundColor'] = backgroundColor

		return JsonResponse(data)



class ExpenseAjaxViewBarBudget(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		data = {}
		days = 7
		start_date = timezone.now().today() #- datetime.timedelta(days=30)

		labels = []
		expense = []		
		budget = []
		backgroundColor = []
		backgroundColor2 = []
		
		dataset = Budget.objects \
			.filter(period__startdate__lte=start_date, period__enddate__gte=start_date) \
			.filter(user=self.request.user) \
			.values('category__name') \
			.annotate(total_amount=Sum('amount')) \
			.order_by('category__name')
			

		for entry in dataset: 
			print (entry['category__name'])
			catname = entry['category__name']
			# catname = 'Antipolo Houses'
			dse = Expense.objects \
				.filter(category__name__iexact=catname) \
				.filter(user=self.request.user) \
				.aggregate(Sum('amount'))	
			# print(dse['amount__sum'])
			labels.append(
					entry['category__name']
				)	
			budget.append(
					entry['total_amount']
				)
			expense.append(
					dse['amount__sum']
				)
			backgroundColor.append(
					"rgba(255, 193, 7, 1)"
				)
			backgroundColor2.append(
					"rgba(108, 117, 125, 1)"
				)


		data['labels'] = labels
		data['budget'] = budget
		data['expense'] = expense	
		data['backgroundColor'] = backgroundColor
		data['backgroundColor2'] = backgroundColor2

		return JsonResponse(data)


