from django.db import models

# Create your models here.
class Product(models.Model):
	product_id=models.IntegerField(default=0)
	product_name=models.CharField(max_length=50)
	price=models.IntegerField(default=0)
	image=models.ImageField(upload_to="images")

	def __str__(self) -> str:
		return self.product_name

