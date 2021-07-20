from django.urls import path, include

from .views import (
    InsuranceProductFilteredTableView,
    InsuranceProductCreateView,
    InsuranceProductUpdateView,
    InsuranceProductResponseFilteredTableView,
    InsuranceProductResponseCreateView
)

app_name = 'insurance'

insurance_product_urlpatterns = ([
    path('table/', InsuranceProductFilteredTableView.as_view(), name='table'),
    path('create/', InsuranceProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', InsuranceProductUpdateView.as_view(), name='update'),
    path('response/table/', InsuranceProductResponseFilteredTableView.as_view(),
         name='response_table'),
    path('<int:pk>/response/create/',
         InsuranceProductResponseCreateView.as_view(), name='response_create'),
], 'product')


urlpatterns = [
    path('product/', include(insurance_product_urlpatterns)),
]
