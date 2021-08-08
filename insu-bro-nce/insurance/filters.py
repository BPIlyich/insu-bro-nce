from django.utils.translation import gettext_lazy as _

import django_filters

from .models import InsuranceProduct, InsuranceProductResponse


class InsuranceProductFilter(django_filters.FilterSet):
    """
    Фильтр для страховых продуктов
    """
    created_at = django_filters.DateRangeFilter()
    name = django_filters.AllValuesFilter()
    percent_rate = django_filters.AllValuesFilter()
    es = django_filters.CharFilter(
        method='filter_elasticsearch', label=_('full-text search'))

    def filter_elasticsearch(self, queryset, name, value):
        """
        "Затычка" для добавления в форму поля полнотекстового поиска
        Логика должны быть реализована в методе get_queryset вьюхи
        """
        return queryset

    class Meta:
        model = InsuranceProduct
        fields = ('es', 'category', 'created_by', 'name', 'percent_rate',
                  'term', 'created_at', 'is_active')


class InsuranceProductResponseFilter(django_filters.FilterSet):
    """
    Фильтр для откликов на страховые продукты
    """
    created_at = django_filters.DateRangeFilter()
    name = django_filters.AllValuesFilter()

    class Meta:
        model = InsuranceProductResponse
        fields = ('insurance_product', 'name', 'created_at')
