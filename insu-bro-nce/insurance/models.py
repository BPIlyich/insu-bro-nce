from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


User = get_user_model()


class InsuranceProductCategory(models.Model):
    """
    Модель категории страхового продукта
    """
    name = models.CharField(_('name'), max_length=100)
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        db_table = 'insurance category'
        verbose_name = _('insurance category')
        verbose_name_plural = _('insurance categories')


class InsuranceProduct(models.Model):
    """
    Модель страхового продукта
    """
    TERM_CHOICES = (
        ('month', _('month')),
        ('year', _('year')),
    )

    category = models.ForeignKey(
        InsuranceProductCategory,
        on_delete=models.CASCADE,
        verbose_name=_('category'),
        related_name='insurance_products'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('created by'),
        related_name='insurance_products'
    )

    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    percent_rate = models.DecimalField(
        _('percent rate'), max_digits=4, decimal_places=2)
    term = models.CharField(_('term'), choices=TERM_CHOICES, max_length=10)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return _('%(name)s by %(created_by)s') % {
            'name': self.name, 'created_by': self.created_by}

    class Meta:
        ordering = ['-created_at']
        db_table = 'insurance_product'
        verbose_name = _('insurance product')
        verbose_name_plural = _('insurance products')


class InsuranceProductResponse(models.Model):
    """
    Модель отклика на страховой продукт
    """
    insurance_product = models.ForeignKey(
        InsuranceProduct,
        on_delete=models.CASCADE,
        verbose_name=_('insurance product'),
        related_name='insurance_responses'
    )

    name = models.CharField(
        pgettext_lazy('user name', 'name'),
        max_length=100,
        help_text=_('What should I call you?')
    )
    email = models.EmailField(_('email'))
    # TODO: валидация номера телефона
    phone = models.CharField(_('phone'), max_length=16)
    comment = models.TextField(_('comment'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        if len(self.comment) < 50:
            return self.comment
        return f'{self.comment:.50}...'

    class Meta:
        ordering = ['-created_at']
        db_table = 'insurance_product_response'
        verbose_name = _('insurance product response')
        verbose_name_plural = _('insurance product responses')
