from django.contrib import admin

from . import models
admin.site.register(models.Example)
admin.site.register(models.Feature)
admin.site.register(models.ImageFeature)
admin.site.register(models.TextFeature)
