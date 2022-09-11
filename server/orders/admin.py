from django.contrib import admin
from .models import Order, OrderItem, Product
from import_export.admin import ImportExportModelAdmin
from import_export import resources


admin.site.register(OrderItem)
class OrderResource(resources.ModelResource):
    """ order resource for import/export data"""
    class Meta:
        model = Order
        fields = ['id', 'total', 'items_count', 'date_stamp', 'time_stamp']                                    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['__str__', 'price']
    search_fields = ['title']
    list_editable = ['price',]
  

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
    #raw_id_fields = ['product', ]
    
    
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    list_display = ['id', 'total', 'items_count', 'date_stamp', 'time_stamp']
    list_filter = ['date_stamp']
    inlines = [OrderItemInline]
