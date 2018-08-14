from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
from .forms import BudgetForm
from .models import Budget

# class BudgetListView(LoginRequiredMixin, ListView):
# 	def get_queryset(self):
# 		return Budget.objects.filter(user=self.request.user)
class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        if filter_val:            
            mybudget = Budget.objects.filter(user=self.request.user).filter(
                    Q(remarks__icontains=filter_val)|                    
                    Q(period__perioddesc__icontains=filter_val)|                    
                    Q(category__name__icontains=filter_val)|
                    Q(category__name__iexact=filter_val)|
                    Q(category__cattype__iexact=filter_val)|
                    Q(category__cattype__icontains=filter_val)
                    ).distinct()
            return mybudget
        else:
            mybudget = Budget.objects.filter(user=self.request.user).distinct()
            return mybudget

    def get_context_data(self, **kwargs):
        context = super(BudgetListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', 'give-default-value')
        return context


class BudgetCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Budget/detail-add.html'
    form_class = BudgetForm
    success_url = '/budget/?q='

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BudgetCreateView, self).form_valid(form)

    def get_queryset(self):
        return Period.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BudgetCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Budget'
        return context

    def get_form_kwargs(self):
        kwargs = super(BudgetCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'budget/detail-update.html'
    form_class = BudgetForm
    success_url = '/budget/?q='

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BudgetUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Budget'
        return context

    def get_form_kwargs(self):
        kwargs = super(BudgetUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'budget/budget_delete.html'
    form_class = BudgetForm
    success_url = '/budget/?q='    

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BudgetDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete Budget'
        return context

    def get_form_kwargs(self):
        kwargs = super(BudgetDeleteView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs