from .models import *
from rest_framework import serializers


class ReferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = RefferBy
        fields = "__all__"
        
class WorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Worker
        fields = "__all__"
        
class AgreementSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Agreement
        fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Payment
        fields = "__all__"
        

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Customer
        fields = "__all__"
        
        
class SubContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = SubContractor
        fields = "__all__"
        
        
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Project
        fields = "__all__"
        
        
class ProjectIntendentSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = ProjectIntendent
        fields = "__all__"