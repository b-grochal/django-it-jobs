from django.contrib import admin
from .models import Job, Application
from django.contrib import admin

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'salary', 'work_type', 'company_name', 'city', 'country')
    list_filter = ('name', 'company_name', 'city', 'country')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'job')
    list_filter = ['job__name']
    search_fields = ['email']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.site_header = "IT Jobs Admin Panel"