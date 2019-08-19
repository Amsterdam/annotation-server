from datapunt_api.serializers import HALSerializer
from rest_framework import serializers

from data_model import models


class StringTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StringTag
        fields = ['key', 'value']


class ExampleSerializer(HALSerializer):
    data_source = serializers.ReadOnlyField(source='name')
    tags = StringTagSerializer(many=True, read_only=True)

    class Meta(object):
        model = models.Example
        fields = '__all__'


class ExampleDetailSerializer(HALSerializer):
    data_source = serializers.ReadOnlyField(source='name')


    class Meta(object):
        model = models.Example
        fields = '__all__'
