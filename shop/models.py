from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name= models.CharField(max_length= 20)
    decs = models.CharField(max_length=100)
    image= models.ImageField(upload_to="shop/images", default='')
    pub_date= models.DateField("")

    def __str__(self):
        return self.product_name