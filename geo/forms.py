from django import forms
from world.models import Province
from world.models import Country
from . import models


class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = [
            "name",
            "province_or_state",
        ]

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields["province_or_state"].queryset = Province.objects.all()



class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = [
            "flag",
            "name",
            "short_name",
            "code",
        ]


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = models.Province
        fields = [
            "name",
            "country",
        ]

    def __init__(self, *args, **kwargs):
        super(ProvinceForm, self).__init__(*args, **kwargs)
        self.fields["country"].queryset = Country.objects.all()

