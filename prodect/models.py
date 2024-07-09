from django.db import models

# Create your models here.
class Products(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=30)
    price =models.FloatField(default=0)
    description=models.TextField(default=0)
    image=models.ImageField(upload_to='media/')
    priorty=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return self.name

