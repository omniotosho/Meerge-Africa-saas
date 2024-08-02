from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("City", api.CityViewSet)
router.register("Country", api.CountryViewSet)
router.register("Province", api.ProvinceViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("world/City/", views.CityListView.as_view(), name="world_City_list"),
    path("world/City/create/", views.CityCreateView.as_view(), name="world_City_create"),
    path("world/City/detail/<int:pk>/", views.CityDetailView.as_view(), name="world_City_detail"),
    path("world/City/update/<int:pk>/", views.CityUpdateView.as_view(), name="world_City_update"),
    path("world/City/delete/<int:pk>/", views.CityDeleteView.as_view(), name="world_City_delete"),
    path("world/Country/", views.CountryListView.as_view(), name="world_Country_list"),
    path("world/Country/create/", views.CountryCreateView.as_view(), name="world_Country_create"),
    path("world/Country/detail/<int:pk>/", views.CountryDetailView.as_view(), name="world_Country_detail"),
    path("world/Country/update/<int:pk>/", views.CountryUpdateView.as_view(), name="world_Country_update"),
    path("world/Country/delete/<int:pk>/", views.CountryDeleteView.as_view(), name="world_Country_delete"),
    path("world/Province/", views.ProvinceListView.as_view(), name="world_Province_list"),
    path("world/Province/create/", views.ProvinceCreateView.as_view(), name="world_Province_create"),
    path("world/Province/detail/<int:pk>/", views.ProvinceDetailView.as_view(), name="world_Province_detail"),
    path("world/Province/update/<int:pk>/", views.ProvinceUpdateView.as_view(), name="world_Province_update"),
    path("world/Province/delete/<int:pk>/", views.ProvinceDeleteView.as_view(), name="world_Province_delete"),

    path("world/htmx/City/", htmx.HTMXCityListView.as_view(), name="world_City_htmx_list"),
    path("world/htmx/City/create/", htmx.HTMXCityCreateView.as_view(), name="world_City_htmx_create"),
    path("world/htmx/City/delete/<int:pk>/", htmx.HTMXCityDeleteView.as_view(), name="world_City_htmx_delete"),
    path("world/htmx/Country/", htmx.HTMXCountryListView.as_view(), name="world_Country_htmx_list"),
    path("world/htmx/Country/create/", htmx.HTMXCountryCreateView.as_view(), name="world_Country_htmx_create"),
    path("world/htmx/Country/delete/<int:pk>/", htmx.HTMXCountryDeleteView.as_view(), name="world_Country_htmx_delete"),
    path("world/htmx/Province/", htmx.HTMXProvinceListView.as_view(), name="world_Province_htmx_list"),
    path("world/htmx/Province/create/", htmx.HTMXProvinceCreateView.as_view(), name="world_Province_htmx_create"),
    path("world/htmx/Province/delete/<int:pk>/", htmx.HTMXProvinceDeleteView.as_view(), name="world_Province_htmx_delete"),
)
