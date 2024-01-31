from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def str(self) -> str:
        return self.name
    

class Product(models.Model):
    name =models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    discounted_price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    
    
    def str(self):
        return self.name
    
    
class Customer(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    
    GENDER_CHOICE=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'OTHERS'),
    ]
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200,blank=True,null=True)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=223)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICE
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete = models.CASCADE)
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cart=models.ForeignKey(Cart,models.CASCADE)
    

class Order(models.Model):
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    
    STATUS_CHOICES=[
        (PENDING_CHOICES,"PENDING"),
        (CONFIRM_CHOICES,"CONFIRM"),
        (CANCEL_CHOICES,"CANCEL"),
        (COMPLETED_CHOICES,"COMPLETED")
    
    ]
    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status=models.CharField(max_length=2,choices=STATUS_CHOICES,default=PENDING_CHOICES)
    payment_status=models.BooleanField(default=False)
    shipping_address=models.CharField(max_length=250)
    
    
class OrderItem(models.Model):
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    
    STATUS_CHOICES=[
        (PENDING_CHOICES,"PENDING"),
        (CONFIRM_CHOICES,"CONFIRM"),
        (CANCEL_CHOICES,"CANCEL"),
        (COMPLETED_CHOICES,"COMPLETED")
    
    ]
    
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=2,default=PENDING_CHOICES,choices=STATUS_CHOICES)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    star=models.IntegerField()



    