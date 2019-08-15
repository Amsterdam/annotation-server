from django.db import models


class Example(models.Model):
    reference = models.CharField(max_length=48, unique=True)


class Feature(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)


class ImageFeature(Feature):
    remote_url = models.URLField()


class TextFeature(Feature):
    remote_url = models.URLField()


class Annotation(models.Model):
    pass
