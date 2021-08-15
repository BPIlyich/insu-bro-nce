from django.contrib.auth import get_user_model

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import InsuranceProduct, InsuranceProductCategory


User = get_user_model()


@registry.register_document
class InsuranceProductDocument(Document):
    """
    TODO: добавить адекватный докстринг
    """
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    created_by = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'company_name': fields.TextField(),
    })

    class Index:
        name = 'insurance_products'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = InsuranceProduct
        fields = ('name', 'description', 'percent_rate', 'term')
        related_models = (InsuranceProductCategory, User)

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, (User, InsuranceProductCategory)):
            return related_instance.insurance_products.all()
