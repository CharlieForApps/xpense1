
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .forms import ExpenseForm
from .models import Expense

# class ExpenseListView(LoginRequiredMixin, ListView):
# 	def get_queryset(self):
# 		return Expense.objects.filter(user=self.request.user)
class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        if filter_val:            
            myexpense = Expense.objects.filter(user=self.request.user).filter(
                    Q(remarks__icontains=filter_val)|
                    Q(category__name__icontains=filter_val)|
                    Q(category__name__iexact=filter_val)|
                    Q(category__cattype__iexact=filter_val)|
                    Q(category__cattype__icontains=filter_val)
                    ).distinct()
            return myexpense
        else:
            myexpense = Expense.objects.filter(user=self.request.user).filter().distinct()
            return myexpense

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', 'give-default-value')
        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'expense/detail-add.html'
    form_class = ExpenseForm
    success_url = '/expense/?q='

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ExpenseCreateView, self).form_valid(form)

    def get_queryset(self):
        return Period.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Expense'
        return context

    def get_form_kwargs(self):
        kwargs = super(ExpenseCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Expense/detail-update.html'
    form_class = ExpenseForm
    success_url = '/expense/?q='

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Expense'
        return context

    def get_form_kwargs(self):
        kwargs = super(ExpenseUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'Expense/expense_delete.html'
    form_class = ExpenseForm
    success_url = '/expense/?q='    

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete Expense'
        return context

    def get_form_kwargs(self):
        kwargs = super(ExpenseDeleteView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs