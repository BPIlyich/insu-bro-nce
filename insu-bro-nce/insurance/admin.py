from django.contrib import admin

from .models import (
    InsuranceProductCategory,
    InsuranceProduct,
    InsuranceProductResponse
)


class InsuranceProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page_view_counter')


admin.site.register(InsuranceProductCategory)
admin.site.register(InsuranceProduct, InsuranceProductAdmin)
admin.site.register(InsuranceProductResponse)
