from django.db import models


class Enterer(models.Model):
    name = models.CharField(max_length=65)
    slug = models.SlugField(max_length=65)

    def __str__(self):
        return self.slug

