from django.contrib import admin
from .models import TransferItem, Transfer, Product, Load, Provider

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', ]
    list_filter = ['name', ]


@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'provider', 'quantity', 'created']
    list_filter = ['created', 'provider',]


class TransferItemInline(admin.TabularInline):
    model = TransferItem
    #raw_id_fields = ['product',]
                                    
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_filter = ['created']
    inlines = [TransferItemInline]
  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'min', 
                    'desired', 'max', 'expire_date', 
                    'days_left', 'status', 'buy_suggestion'
    ]
    list_filter = ['name', 'quantity']
