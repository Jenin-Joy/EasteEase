from django.db import models
from Owner.models import*
from Guest.models import*


class tbl_bookproperty(models.Model):
    bookproperty_date=models.DateField(auto_now_add=True)
    bookproperty_amount=models.CharField(max_length=50)
    bookproperty_sellproperty_id=models.ForeignKey(tbl_sellproperty,on_delete=models.CASCADE)
    bookpropertyuser_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    bookproperty_status=models.IntegerField(default=0)
    

class tbl_complaint(models.Model):
    complaint_id=models.CharField(max_length=50) 
    complaint_title=models.CharField(max_length=50)  
    complaint_date=models.DateField(auto_now_add=True)  
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=50) 
    owner=models.ForeignKey(tbl_owner,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)

class tbl_rentbooking(models.Model):
    rentbooking_date=models.DateField(auto_now_add=True)
    rentbooking_amount=models.CharField(max_length=50)
    rentbooking_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    rentbooking_fdate = models.DateField()
    rentbooking_tdate = models.DateField()
    rentproperty=models.ForeignKey(tbl_rentproperty,on_delete=models.CASCADE)



class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    owner_from = models.ForeignKey(tbl_owner,on_delete=models.CASCADE,related_name="owner_from",null=True)
    owner_to = models.ForeignKey(tbl_owner,on_delete=models.CASCADE,related_name="owner_to",null=True)