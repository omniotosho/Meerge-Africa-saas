from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class City(models.Model):

    # Relationships
    province_or_state = models.ForeignKey("geo.Province", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'cities'
        verbose_name = 'cities'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("world_City_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("world_City_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("world_City_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("world_City_htmx_delete", args=(self.pk,))


class Country(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    flag = models.ImageField(upload_to="upload/images/")
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.SmallIntegerField()

    class Meta:
        db_table = "countries"
        verbose_name = 'countries'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("world_Country_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("world_Country_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("world_Country_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("world_Country_htmx_delete", args=(self.pk,))


class Province(models.Model):

    # Relationships
    # country = models.ForeignKey("geo.Country", on_delete=models.CASCADE)
    country = CountryField()

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("world_Province_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("world_Province_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("world_Province_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("world_Province_htmx_delete", args=(self.pk,))
