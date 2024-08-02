from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CityViewSet(viewsets.ModelViewSet):
    """ViewSet for the City class"""

    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Country class"""

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProvinceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Province class"""

    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    permission_classes = [permissions.IsAuthenticated]
