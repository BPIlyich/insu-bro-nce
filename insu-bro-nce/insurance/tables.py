from django.utils.translation import gettext_lazy as _

import django_tables2 as tables

from .utils import build_link
from .models import InsuranceProduct, InsuranceProductResponse


class InsuranceProductTable(tables.Table):
    """
    Таблица страховых продуктов
    """
    get_action = tables.Column(
        verbose_name=_('actions'), orderable=False, accessor='pk')

    def render_get_action(self, record):
        if self.request.user != record.created_by:
            return build_link(
                record.get_response_creation_url(), text=_('response'))
        else:
            return build_link(record.get_update_url(), text=_('update'))

    class Meta:
        model = InsuranceProduct
        sequence = ('category', 'created_by', 'name', 'description', 'term',
                    'percent_rate', 'created_at', 'is_active', 'get_action')
        exclude = ('id', 'updated_at')


class InsuranceProductResponseTable(tables.Table):
    """
    Таблица откликов на страховые продукты
    """

    class Meta:
        model = InsuranceProductResponse
        sequence = ('insurance_product', 'name', 'email',
                    'phone', 'comment', 'created_at')
        exclude = ('id', )
