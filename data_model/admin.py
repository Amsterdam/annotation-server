from django.contrib import admin

from . import models
admin.site.register(models.DataSource)
admin.site.register(models.Example)
admin.site.register(models.Feature)
admin.site.register(models.ImageFeature)
admin.site.register(models.TextFeature)
admin.site.register(models.Annotation)
admin.site.register(models.Label)
admin.site.register(models.TextLabel)
