from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Sale
                      
class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale
        fields = ['date', 'amount']

class SaleAdmin(ImportExportModelAdmin):
    resource_class = SaleResource

admin.site.register(Sale, SaleAdmin)
