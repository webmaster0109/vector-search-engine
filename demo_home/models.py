from django.db import models

# Create your models here.

class VectorProduct(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    sku = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.URLField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "demo_products"
        unique_together = ('title', 'brand', 'category')
        verbose_name = "Product"
        verbose_name_plural = "Product"


    def __str__(self):
        return self.title