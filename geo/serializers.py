from rest_framework import serializers

from . import models


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = [
            "created",
            "last_updated",
            "name",
            "province_or_state",
        ]

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = [
            "created",
            "flag",
            "name",
            "short_name",
            "last_updated",
            "code",
        ]

class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Province
        fields = [
            "last_updated",
            "created",
            "name",
            "country",
        ]
