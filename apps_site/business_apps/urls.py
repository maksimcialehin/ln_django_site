from django.urls import path
from django_filters.views import FilterView
from .views import AppListView, AppDetailView, AppListOrdered


urlpatterns = [
    path('', AppListView.as_view(), name='home'),
    path('app_info/<int:app_id>', AppDetailView.as_view(), name='app_info'),
    path('app_info/sort_by_year', AppListOrdered.as_view(), name='by_year'),
]
