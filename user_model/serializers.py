from rest_framework import serializers

from . import models


class AnnotationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnnotationUser
        fields = ['username']
