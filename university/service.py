from django_filters import rest_framework as filters
from .models import University

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    state_univers = CharFilterInFilter(field_name='benefits_univers__state_univers', lookup_expr='in')
    arm_univers = CharFilterInFilter(field_name='benefits_univers__arm_univers', lookup_expr='in')
    tech_univers = CharFilterInFilter(field_name='benefits_univers__tech_univers', lookup_expr='in')
    humanitarian_univers = CharFilterInFilter(field_name='benefits_univers__humanitarian_univers', lookup_expr='in')
    hostel_univers = CharFilterInFilter(field_name='benefits_univers__hostel_univers', lookup_expr='in')

    class Meta:
        model = University
        fields = ['city', 'state_univers', 'arm_univers', 'tech_univers', 'humanitarian_univers', 'hostel_univers']

