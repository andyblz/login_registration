# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
  name = models.CharField(max_length=255)
  alias = models.CharField(max_length=45)
  email = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
def __repr__(self):
        return "<Users object: {} {} {}>".format(self.name, self.alias, self.email)