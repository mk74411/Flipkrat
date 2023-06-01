from django.shortcuts import render
from customer.models import *
from customer.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class GetCustomerView(APIView):
    def get(self,request):
       instance = Customers.objects.all()
       print("instance",instance)
       ser = GetCustomerSerializers(instance,many=True)
       print("ser",ser.data)
       return Response(ser.data)
    
    def post(self,request):
        params=request.data
        print("data",params)
        ser=GetCustomerSerializers(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"Message":"Save Successfully"})

class GetAddressView(APIView):
    def get(self,request):
       instance = CustomerAddress.objects.all()
       print("instance",instance)
       ser = GetAddressSerializer(instance,many=True)
       return Response(serializers.data)
class CustomerDetailsAddressView(APIView):

    def get(self,request,pk):
        instance = Customers.objects.filter(id=pk)
        serializers = CustomerDetailsAddressSerializers(instance,many=True)
        return Response(serializers.data)
    
    
