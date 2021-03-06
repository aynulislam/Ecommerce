from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=100)
    catagory = models.CharField(max_length=10)
    buying_price = models.DecimalField(max_digits=5, decimal_places=2)
    selling_price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='product')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name





class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    status = models.BooleanField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_qty = models.IntegerField()
    remain_qty = models.IntegerField()
    status = models.BooleanField(default=False)
    created_by = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    


