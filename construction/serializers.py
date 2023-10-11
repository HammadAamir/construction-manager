from .models import *
from rest_framework import serializers
from construction_manager import settings

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
    payment_records = serializers.SerializerMethodField("get_payment")

    class Meta:
        model = Agreement
        fields = "__all__"

    def get_payment(self, obj):
        payment_ls = []
        payments = Payment.objects.filter(agreement_id=obj.id)
        if payments.exists():
            for payment in payments:
                payment_ls.append({
                    "check_no": payment.check_no,
                    "date": payment.date,
                    "amount": payment.amount
                })
            return payment_ls
        else:
            return payment_ls


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
    images = serializers.SerializerMethodField("get_image")
    workers = serializers.SerializerMethodField("get_worker")


    class Meta:
        model = DailyWork
        fields = "__all__"

    def get_image(self, obj):
        image_ls = []
        images = DailyWorkImage.objects.filter(work=obj.id)
        if images.exists():
            for image in images:
                image_ls.append(settings.MY_BASE_URL+"/"+image.project_image)
            return image_ls
        else:
            return image_ls

    def get_worker(self, obj):
        worker_ls = []
        workers = DailyWorker.objects.filter(work=obj.id)
        if workers.exists():
            for worker in workers:
                worker_ls.append(worker.worker.full_name)
            return worker_ls
        else:
            return worker_ls


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