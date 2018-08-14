from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
from .forms import CategoryForm
from .models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    # paginate_by = 10
    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        if filter_val:            
            mycategory = Category.objects.filter(user=self.request.user).filter(
                    Q(name__icontains=filter_val)|
                    Q(cattype__icontains=filter_val)
                    ).distinct()
            # user_list = User.objects.all()
            # paginator = Paginator(mycategory, 10)
            return mycategory
        else:
            mycategory = Category.objects.filter(user=self.request.user).filter().distinct()
            return mycategory

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', 'give-default-value')
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category/detail-add.html'
    form_class = CategoryForm
    success_url = '/category/?q='

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Category'
        return context

    def get_form_kwargs(self):
        kwargs = super(CategoryCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category/detail-update.html'
    form_class = CategoryForm
    success_url = '/category/?q='

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Category'
        return context

    def get_form_kwargs(self):
        kwargs = super(CategoryUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'category/category_delete.html'
    form_class = CategoryForm
    success_url = '/category/?q='    

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete Category'
        return context

    def get_form_kwargs(self):
        kwargs = super(CategoryDeleteView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs