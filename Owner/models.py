from django.db import models
from Admin.models import*
from Guest.models import*


class tbl_rentproperty(models.Model):
    rentproperty_location=models.CharField(max_length=50)
    rentproperty_type=models.CharField(max_length=50)
    rentproperty_rentaltype=models.CharField(max_length=50)
    rentproperty_price=models.CharField(max_length=50)
    rentproperty_photo=models.FileField(upload_to='Assets/owner/photo')
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE)

class tbl_sellproperty(models.Model):
    sellproperty_location=models.CharField(max_length=50)
    sellproperty_type=models.CharField(max_length=50)
    sellproperty_price=models.CharField(max_length=50)
    sellproperty_photo=models.FileField(upload_to='Assets/owner/photo')
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE)
