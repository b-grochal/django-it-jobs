from .models import Job, Application
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
       model = Application
       fields = ['pk', 'first_name', 'last_name', 'email', 'phone_number', 'city_of_residence', 'country_of_residence', 'personal_description', 'job']