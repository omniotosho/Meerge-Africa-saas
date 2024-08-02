from django.contrib import admin
from django import forms

from . import models


class CityAdminForm(forms.ModelForm):

    class Meta:
        model = models.City
        fields = "__all__"


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = [
        "created",
        "last_updated",
        "name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "name",
    ]


class CountryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Country
        fields = "__all__"


class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm
    list_display = [
        "created",
        "flag",
        "name",
        "short_name",
        "last_updated",
        "code",
    ]
    readonly_fields = [
        "created",
        "flag",
        "name",
        "short_name",
        "last_updated",
        "code",
    ]


class ProvinceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Province
        fields = "__all__"


class ProvinceAdmin(admin.ModelAdmin):
    form = ProvinceAdminForm
    list_display = [
        "last_updated",
        "created",
        "name",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "name",
    ]


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Province, ProvinceAdmin)
