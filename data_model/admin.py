from django.contrib import admin

from . import models


class StringTagInline(admin.TabularInline):
    model = models.StringTag


class ExampleAdmin(admin.ModelAdmin):
    list_display = ('reference', 'data_source', 'description')
    inlines = [
        StringTagInline
    ]


class ImageFeatureAdmin(admin.ModelAdmin):
    list_display = ('example', 'remote_url')


admin.site.register(models.Example, ExampleAdmin)
admin.site.register(models.StringTag)
admin.site.register(models.DataSource)
admin.site.register(models.Feature)
admin.site.register(models.ImageFeature, ImageFeatureAdmin)
admin.site.register(models.TextFeature)
admin.site.register(models.Annotation)
