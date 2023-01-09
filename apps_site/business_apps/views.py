from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import AppFilter

from .models import App


class AppListView(FilterView):
    model = App
    template_name = 'business_apps/index.html'
    context_object_name = 'apps'
    paginate_by = 10
    filterset_class = AppFilter

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'id')
        new_context = App.objects.all().order_by(order)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super(AppListView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'id')
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)


class AppListOrdered(ListView):
    model = App
    template_name = 'business_apps/index.html'
    context_object_name = 'apps'
    paginate_by = 2

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'id')
        return App.objects.all().order_by(order)


class AppDetailView(DetailView):
    model = App
    template_name = 'business_apps/app_info.html'
    context_object_name = 'app'
    pk_url_kwarg = 'app_id'

    def get_queryset(self):
        return super().get_queryset()
