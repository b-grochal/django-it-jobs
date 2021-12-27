from django.contrib import admin
from .models import Job, Application
from django.contrib import admin

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'salary', 'work_type', 'company_name', 'city', 'country')
    list_filter = ('name', 'company_name', 'city', 'country')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "IT Jobs Admin Panel"