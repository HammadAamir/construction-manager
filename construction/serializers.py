from .models import *
from rest_framework import serializers


class ReferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RefferBy
        fields = "__all__"
        
class WorkerSerializer(serializers.ModelSerializer):
    reference = serializers.SerializerMethodField("get_reference")
    
    class Meta:
        model = Worker
        fields = "__all__"

    def get_reference(self, obj):
        return obj.reffer_by.name
        
class AgreementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agreement
        fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = "__all__"
        

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"
        
        
class SubContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubContractor
        fields = "__all__"
        
        
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = "__all__"


class DailyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWork
        fields = "__all__"


class DailyWorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWorkImage
        fields = "__all__"


class DailyWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWorker
        fields = "__all__"


class DailyWorkerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWorkImage
        fields = "__all__"