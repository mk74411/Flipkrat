from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    age=models.Field(max_length=15,null=True,blank=True)
    address=models.IntegerField(max_length=15,null=True,blank=True)
    
    def __self__(self):
        return self.first_name
class CustomerAddress(models.Model):
     customer=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,related_name="customer_addresses")
     street_name=models.CharField(max_length=15,null=True,blank=True)
     street_number=models.IntegerField(null=True,blank=True)
     city=models.CharField(max_length=15,null=True,blank=True)
     country=models.CharField(max_length=15,null=True,blank=True)
     pincode=models.IntegerField(null=True,blank=True)
     def __self__(self):
        return self.street_name
class CustomerAadhar(models.Model):
    customer=models.OneToOneField(Customers,on_delete=models.CASCADE)
    aadhar_number=models.IntegerField
    aadhar_name=models.CharField(max_length=15)
    def __self__(self):
        return self.aadhar_name



     
     

    
    

