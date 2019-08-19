from datapunt_api.rest import DatapuntViewSet

from data_model import models, serializers


class ExampleViewSet(DatapuntViewSet):
    queryset = models.Example.objects.all()
    serializer_class = serializers.ExampleSerializer
    serializer_detail_class = serializers.ExampleSerializer
