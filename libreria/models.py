from tkinter.messagebox import YES
from unicodedata import category
from warnings import resetwarnings
from django.db import models
from django.db.models import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.files import ImageField
from django.conf import settings

# This is the real date of the product creation
from datetime import datetime, date


# Create your models here.

class product(models.Model):
   
   id = models.AutoField(
      primary_key=True
      )
   name = models.CharField(
      max_length=50, 
      verbose_name="Name" 
      )
   category = models.TextField(
      null=True,
      max_length=50,
      blank=True,
      verbose_name="Category"
      )
   description = models.TextField(
      null=True, 
      verbose_name="Description"
      )
   location = models.CharField(
      max_length=30,
      verbose_name="Location",
      null=True,
      )
   # null=True means that the field is not required
   purchase_cost = models.DecimalField(
      max_digits=5, 
      decimal_places=2,
      null=True, 
      verbose_name="Purchase Cost"
      )
   sale_cost = models.DecimalField(
      max_digits=5, 
      decimal_places=2, 
      blank=True, 
      verbose_name="Sale cost"
    )
   upload_date = models.DateField(
      auto_now_add=True
      )
   # blank=True means that the field is not required
   sale_date = models.DateField(
      blank=True
      )
   imagen = models.ImageField(
      upload_to='imagen/', 
      null=True, 
      verbose_name="Imagen"
      )
   # This amount is in percentage 
   intermediary_cost = models.IntegerField(
      blank=True,   
      verbose_name="Intermediary cost"
      )
   profit = models.DecimalField(
      max_digits =5, 
      decimal_places=2, 
      blank=True,  
      verbose_name="Profit"
      )
   sold = models.BooleanField()
   
   
   
   def __str__(self):
      fila = "id: " + str(self.id) + " name: " + self.name + " description: " + self.description + " ubication: " + self.ubication + " purchase_cost: " + str(self.purchase_cost) + " sale_cost: " + str(self.sale_cost) + " upload_date: " + str(self.upload_date) + " sale_date: " + str(self.sale_date) + " imagen: " + str(self.imagen) + " intermediary_cost: " + str(self.intermediary_cost) + " profit: " + str(self.profit) + " sold: " + str(self.sold)  +str(self.category)
      return fila
   
# This function is executed every time a product is deleted

   def delete(self, using=None, keep_parents=False):
      self.imagen.storage.delete(self.imagen.name)
      super().delete()
   
# This function is executed every time a product is saved

   def save (self, *args, **kwargs):
      self.subtration = self.sale_cost - self.purchase_cost
      self.percentage = self.intermediary_cost * self.subtration / 100
      self.profit = self.subtration - self.percentage
      super(product, self).save(*args, **kwargs)