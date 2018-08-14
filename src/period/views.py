
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
from .forms import PeriodForm
from .models import Period

# class PeriodListView(LoginRequiredMixin, ListView):
# 	def get_queryset(self):
# 		return Period.objects.filter(user=self.request.user)
class PeriodListView(LoginRequiredMixin, ListView):
    model = Period
    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        if filter_val:            
            myperiod = Period.objects.fileter(user=self.request.user).filter(
                    Q(perioddesc__icontains=filter_val)
                    ).distinct()
            return myperiod
        else:
            myperiod = Period.objects.filter(user=self.request.user).filter().distinct()
            return myperiod

    def get_context_data(self, **kwargs):
        context = super(PeriodListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', 'give-default-value')
        return context


class PeriodCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Period/detail-add.html'
    form_class = PeriodForm
    success_url = '/period/?q='

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(PeriodCreateView, self).form_valid(form)

    def get_queryset(self):
        return Period.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(PeriodCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Period'
        return context

    def get_form_kwargs(self):
        kwargs = super(PeriodCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PeriodUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Period/detail-update.html'
    form_class = PeriodForm
    success_url = '/period/?q='

    def get_queryset(self):
        return Period.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(PeriodUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Period'
        return context

    def get_form_kwargs(self):
        kwargs = super(PeriodUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PeriodDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'Period/Period_delete.html'
    form_class = PeriodForm
    success_url = '/period/?q='    

    def get_queryset(self):
        return Period.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(PeriodDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete Period'
        return context

    def get_form_kwargs(self):
        kwargs = super(PeriodDeleteView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs