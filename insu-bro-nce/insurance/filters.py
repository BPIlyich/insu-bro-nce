import django_filters

from .models import InsuranceProduct, InsuranceProductResponse


class InsuranceProductFilter(django_filters.FilterSet):
    """
    Фильтр для страховых продуктов
    """
    created_at = django_filters.DateRangeFilter()
    name = django_filters.AllValuesFilter()
    percent_rate = django_filters.AllValuesFilter()

    class Meta:
        model = InsuranceProduct
        fields = ('category', 'created_by', 'name', 'percent_rate',
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
