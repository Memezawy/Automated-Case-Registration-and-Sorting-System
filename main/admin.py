from django.contrib import admin
from .models import Refugee, Service, Nationality, Service2


class RefugeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_no', 'service', 'service2', 'nationality', 'case_status', 'data_created')

    actions = ['close_case', 'open_case', 'pend_case']

    def close_case(self, request, queryset):
        queryset.update(case_status='Closed')

    def open_case(self, request, queryset):
        queryset.update(case_status='Open')

    def pend_case(self, request, queryset):
        queryset.update(case_status='Pending')


# Register your models here.
admin.site.site_title = "Admin Page"
admin.site.site_header = "UNHCR Form Adminstration"
admin.site.register(Refugee, RefugeeAdmin)
admin.site.register(Nationality)
