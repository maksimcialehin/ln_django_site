from django.db import models
from django.urls import reverse


class App(models.Model):
    app_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField()

    def __str__(self) -> str:
        return self.app_name

    def get_absolute_url(self):
        return reverse("app_info", kwargs={"app_id": self.pk})

    class Meta:
        verbose_name = 'Business Apps'
        # ordering = ['app_name', 'release_year']    
