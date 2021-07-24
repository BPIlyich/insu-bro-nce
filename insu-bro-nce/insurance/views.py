from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import InsuranceProduct, InsuranceProductResponse
from .filters import InsuranceProductFilter, InsuranceProductResponseFilter
from .tables import InsuranceProductTable, InsuranceProductResponseTable


class InsuranceProductFilteredTableView(SingleTableMixin, FilterView):
    """
    View с фильтруемой таблицей страховых продуктов
    """
    table_class = InsuranceProductTable
    model = InsuranceProduct
    template_name = 'table_with_filter.html'
    filterset_class = InsuranceProductFilter
    extra_context = {'title': _('Insurance products')}


class InsuranceProductCreateView(
        LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View для создания страхового продукта
    """
    model = InsuranceProduct
    fields = ('category', 'name', 'description', 'percent_rate', 'term')
    template_name = 'form.html'
    success_message = _(
        'Insurance product "%(name)s" was created successfully')
    success_url = reverse_lazy('base')
    extra_context = {'title': _('Create insurance product')}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InsuranceProductUpdateView(
        LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View для редактирования страхового продукта
    """
    model = InsuranceProduct
    fields = ('category', 'name', 'description',
              'percent_rate', 'term', 'is_active')
    template_name = 'form.html'
    success_message = _(
        'Insurance product "%(name)s" was updated successfully')
    success_url = reverse_lazy('base')
    extra_context = {'title': _('Update insurance product')}

    def get_queryset(self, *args, **kwargs):
        """
        Редактирование доступно только автору
        """
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(created_by=self.request.user)


class InsuranceProductResponseFilteredTableView(
        LoginRequiredMixin, SingleTableMixin, FilterView):
    """
    View с фильтруемой таблицей страховых продуктов
    """
    table_class = InsuranceProductResponseTable
    model = InsuranceProductResponse
    template_name = 'table_with_filter.html'
    filterset_class = InsuranceProductResponseFilter
    extra_context = {'title': _('Insurance product responces')}

    def get_queryset(self, *args, **kwargs):
        """
        Просмотр отзывов доступен только авторам страховых продуктов
        """
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(
                insurance_product__created_by=self.request.user)


class InsuranceProductResponseCreateView(SuccessMessageMixin, CreateView):
    """
    View для создания отклика на страховой продукт
    """
    template_name = 'form.html'
    model = InsuranceProductResponse
    fields = ('insurance_product', 'comment', 'name', 'email', 'phone')
    success_message = _(
        'Response for insurance product "%(insurance_product)s" '
        'was created successfully'
    )
    success_url = reverse_lazy('base')
    extra_context = {'title': _('Create response for insurance product')}

    def get_initial(self):
        initial = super().get_initial()
        initial['insurance_product'] = get_object_or_404(
            InsuranceProduct, pk=self.kwargs['pk'])
        return initial
