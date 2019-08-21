from datapunt_api.rest import DatapuntViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from data_model import models, serializers


class ExampleViewSet(DatapuntViewSet):
    queryset = models.Example.objects.all()
    serializer_class = serializers.ExampleListSerializer
    serializer_detail_class = serializers.ExampleDetailSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['reference', 'description', 'tags']
    filterset_fields = ['reference', 'description', 'tags__key']
    filterset_fields = ['reference', 'description', 'tags__value']
