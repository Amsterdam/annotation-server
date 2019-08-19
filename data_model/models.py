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

    # meta = JSONField(default=meta_default)

    def __str__(self):
        return self.reference


class StringTag(models.Model):
    # example = models.ForeignKey(Example, on_delete=models.CASCADE, related_name='tags')
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.key}: {self.value}'

    # class Meta:
    #     unique_together = ['example', 'key']


class Feature(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)


class ImageFeature(Feature):
    remote_url = models.URLField()


class TextFeature(Feature):
    body = models.TextField()

    def __str__(self):
        return self.body[:80]


class Annotation(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)
    tag = models.ForeignKey(StringTag, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'annotation {self.example}: {self.tag}'


