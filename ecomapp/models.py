from django.db import models

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=20)

    def __str__(self):
        return self.c_name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='products')
    uploaddate = models.DateTimeField(auto_now=True)
    stk_available = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_relname')

    def __str__(self):
        return f'{self.name}, {self.description}'
    

class Cartitems(models.Model):
    item = models.ManyToManyField(Product)
    

