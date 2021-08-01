from django.contrib import admin

from .models import (
    InsuranceProductCategory,
    InsuranceProduct,
    InsuranceProductResponse
)


admin.site.register(InsuranceProductCategory)
admin.site.register(InsuranceProduct)
admin.site.register(InsuranceProductResponse)
