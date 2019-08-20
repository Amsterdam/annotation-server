from django.contrib.postgres.fields import JSONField
from django.db import models

from annotation_server import settings


class DataSource(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


def meta_default():
    return {}


class Example(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    reference = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=64)

    tags = models.ManyToManyField('StringTag', through='Annotation')

    # Note, to get the latest tags per key, the following query works:
    # `myExample.tags(manager='latest').all()`
    # To get the default use:
    # `myExample.tags(manager='objects').all()`

    def __str__(self):
        return self.reference


class LatestTagManager(models.Manager):
    def get_queryset(self):
        return super(LatestTagManager, self) \
            .get_queryset() \
            .filter() \
            .order_by('key', '-annotation__modified_at') \
            .distinct('key')


class StringTag(models.Model):
    # example = models.ForeignKey(Example, on_delete=models.CASCADE, related_name='tags')
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=128)

    # Managers
    objects = models.Manager()  # The default manager.
    latest = LatestTagManager()

    def __str__(self):
        return f'{self.key}: {self.value}'


class Feature(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)


class ImageFeature(Feature):
    remote_url = models.URLField()


class TextFeature(Feature):
    body = models.TextField()

    def __str__(self):
        return self.body[:80]


# Latest annotations
class LatestAnnotationManager(models.Manager):
    def get_queryset(self):
        return super(LatestAnnotationManager, self)\
            .get_queryset()\
            .filter()\
            .order_by('tag__key', '-modified_at')\
            .distinct('tag__key')


class Annotation(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE, related_name='annotations')
    tag = models.ForeignKey(StringTag, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()  # The default manager.
    latest = LatestAnnotationManager()  # The EmployeeManager manager.

    def __str__(self):
        return f'annotation {self.example}: {self.tag}'

    class Admin:
        manager = 'objects'
