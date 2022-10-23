from django.db import models


class Screen(models.Model):
    address = models.CharField("Address where screen is located", max_length=256, null=True, blank=True)
    resolution = models.CharField("Resolution", max_length=12, null=True, blank=True)
    diagonal = models.FloatField("Diagonal", null=True, blank=True)

    def __str__(self):
        return f'Screen at "{self.address}"'

    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"
