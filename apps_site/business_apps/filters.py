import django_filters
from .models import App


class AppFilter(django_filters.FilterSet):
    app_name = django_filters.CharFilter(field_name='app_name', lookup_expr='icontains')
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='release_year')
    year__gt = django_filters.NumberFilter(field_name='release_year', lookup_expr='gt')
    year__lt = django_filters.NumberFilter(field_name='release_year', lookup_expr='lt')

    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('release_year', 'Release year'),
        ),

        # labels do not need to retain order
        field_labels={
            'release_year': 'Release year',
        }
    )

    class Meta:
        model = App
        fields = ['app_name', 'company_name']
