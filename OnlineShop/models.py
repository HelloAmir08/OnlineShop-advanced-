from django.db import models
from decimal import Decimal


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            discount_amount = (self.price * Decimal(self.discount)) / Decimal(100)
            return self.price - discount_amount
        return self.price

    @property
    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return self.name

class Comment(BaseModel):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.email


