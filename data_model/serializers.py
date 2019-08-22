from datapunt_api.serializers import HALSerializer
from rest_framework import serializers

from data_model import models


class StringTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StringTag
        fields = ['key', 'value']


class AnnotationSerializer(serializers.ModelSerializer):
    tag = StringTagSerializer(read_only=True)

    class Meta:
        model = models.Annotation
        fields = ['tag', 'author', 'created_at', 'modified_at']


class ExampleListSerializer(HALSerializer):
    tags = StringTagSerializer(many=True, read_only=True)
    latest_tags = serializers.SerializerMethodField('get_latest_tags')
    annotations = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    def get_latest_tags(self, example):
        items = example.tags(manager='latest').all()
        serializer = StringTagSerializer(instance=items, many=True, read_only=True)
        return serializer.data

    class Meta(object):
        model = models.Example
        fields = ['id', 'reference', '_links', 'tags', 'latest_tags', 'annotations']


class ExampleDetailSerializer(HALSerializer):
    data_source = serializers.ReadOnlyField(source='name')
    tags = StringTagSerializer(many=True, read_only=True)
    latest_tags = serializers.SerializerMethodField('get_latest_tags')
    annotations = AnnotationSerializer(read_only=True, many=True)

    def get_latest_tags(self, example):
        items = example.tags(manager='latest').all()
        serializer = StringTagSerializer(instance=items, many=True, read_only=True)
        return serializer.data

    class Meta(object):
        model = models.Example
        fields = '__all__'
