from .models import Job, Application
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField()
    class Meta:
       model = Application
       fields = '__all__'