from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    @property
    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return self.name

class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.ONE.value)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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


