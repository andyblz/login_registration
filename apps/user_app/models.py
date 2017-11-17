# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..LR_app.models import Users 

from django.db import models


class Authors(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
     return "<authors object: {} {}>".format(self.name, self.books)

class Books(models.Model):
  title = models.CharField(max_length=255)
  uploader = models.ForeignKey(Users, related_name = "uploaded_book")
  author = models.ForeignKey(Authors, related_name = "books")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
     return "<Books object: {} {}>".format(self.title, self.uploader)

class Reviews(models.Model):
  rating = models.IntegerField()
  comments = models.TextField(max_length=1000)
  reviewer = models.ForeignKey(Users, related_name = "reviews")
  book = models.ForeignKey(Books, related_name = "reviews")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
     return "<Reviews object:{} {} {} {}>".format(self.rating, self.comments, self.reviewer, self.book)


