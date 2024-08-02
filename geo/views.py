from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CityListView(generic.ListView):
    model = models.City
    form_class = forms.CityForm


class CityCreateView(generic.CreateView):
    model = models.City
    form_class = forms.CityForm


class CityDetailView(generic.DetailView):
    model = models.City
    form_class = forms.CityForm


class CityUpdateView(generic.UpdateView):
    model = models.City
    form_class = forms.CityForm
    pk_url_kwarg = "pk"


class CityDeleteView(generic.DeleteView):
    model = models.City
    success_url = reverse_lazy("world_City_list")


class CountryListView(generic.ListView):
    model = models.Country
    form_class = forms.CountryForm


class CountryCreateView(generic.CreateView):
    model = models.Country
    form_class = forms.CountryForm


class CountryDetailView(generic.DetailView):
    model = models.Country
    form_class = forms.CountryForm


class CountryUpdateView(generic.UpdateView):
    model = models.Country
    form_class = forms.CountryForm
    pk_url_kwarg = "pk"


class CountryDeleteView(generic.DeleteView):
    model = models.Country
    success_url = reverse_lazy("world_Country_list")


class ProvinceListView(generic.ListView):
    model = models.Province
    form_class = forms.ProvinceForm


class ProvinceCreateView(generic.CreateView):
    model = models.Province
    form_class = forms.ProvinceForm


class ProvinceDetailView(generic.DetailView):
    model = models.Province
    form_class = forms.ProvinceForm


class ProvinceUpdateView(generic.UpdateView):
    model = models.Province
    form_class = forms.ProvinceForm
    pk_url_kwarg = "pk"


class ProvinceDeleteView(generic.DeleteView):
    model = models.Province
    success_url = reverse_lazy("world_Province_list")
