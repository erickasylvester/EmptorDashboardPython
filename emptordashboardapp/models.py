# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.user