from django.contrib.postgres.fields import JSONField
from django.db import models
from djchoices import DjangoChoices, ChoiceItem


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

    meta = JSONField(default=meta_default)

    def __str__(self):
        return self.reference


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

    def __str__(self):
        return f'annotation {self.example}, label(s): {self.label_set.all()}'


class Label(models.Model):
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE, blank=True, null=True)


class MultiLabelChoice(DjangoChoices):
    # Used for multi class annotations, so label is mutually exclusive. Something is an apple or a pear. Not both.
    exclusive = ChoiceItem()

    # Used for multi label annotations. A meal might contain carbs, fats, proteins and so on.
    multiple = ChoiceItem()


class TextLabel(Label):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64, choices=MultiLabelChoice.choices, default=MultiLabelChoice.exclusive)
    group = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name} ({self.type})'
