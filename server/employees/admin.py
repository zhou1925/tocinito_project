from django.contrib import admin
from .models import Team, Employee, Role

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'birthday', 'document_id']
    list_filter = ['name', ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name', ]

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]