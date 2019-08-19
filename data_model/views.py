from datapunt_api.rest import DatapuntViewSet
from django_filters.rest_framework import DjangoFilterBackend

from data_model import models, serializers


class ExampleViewSet(DatapuntViewSet):
    queryset = models.Example.objects.all()
    serializer_class = serializers.ExampleSerializer
    serializer_detail_class = serializers.ExampleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reference', 'description', 'tags', 'tags__key', 'tags__value']
