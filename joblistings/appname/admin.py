from django.contrib import admin

# Register your models here.

from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'salary')
    list_filter = ('location',)
    search_fields = ('title', 'description', 'location')
    list_per_page = 10

#un: admin
#pw: testadmin123
admin.site.register(Job, JobAdmin)