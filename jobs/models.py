from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    salary = model.CharField(max_length=255)
    work_type = model.CharField(max_length=255)
    company_name = model.CharField(max_length=255)
    description = model.TextField()
    city = model.CharField(max_length=255)
    country = model.CharField(max_length=255)

class Application(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    city_of_residence = models.CharField(max_length=255)
    country_of_residence = models.CharField(max_length=255)
    personal_description = model.TextField()