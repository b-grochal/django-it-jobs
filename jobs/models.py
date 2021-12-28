from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    work_type = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s - %s - %s' % (self.company_name, self.name, self.city, self.country)

class Application(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    city_of_residence = models.CharField(max_length=255)
    country_of_residence = models.CharField(max_length=255)
    personal_description = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', related_query_name='application')