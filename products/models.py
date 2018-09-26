import random
import os
from django.db import models
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename)
 

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True) 

class FeaturedManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def featured(self):
        return self.get_queryset().featured() #filter(featured=True)

class Product(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = FeaturedManager()

    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_detail',args=[self.slug])    