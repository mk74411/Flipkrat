from rest_framework import serializers
from customer.models import *

class GetCustomerSerializers(serializers.Serializer):
    class Meta:
        model=Customers
        fields="__all__"

class GetAddressSerializer(serializers.ModelSerializer):
     
     class Meta:
        model=CustomerAddress
        fields="__all__"

class CustomerDetailsAddressSerializers(serializers.ModelsSerializer):
    customer_addresses=GetAddressSerializer(many=True)
    class Meta:
     model = Customers
     field=('first_name','last_name',' mobile','age','address')

