from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Txnn

class CustomerAdmin(admin.ModelAdmin):
    list_display    = ('user_id', 'name', 'email')
    search_fields   = ('name', 'email')
    readonly_fields = ()
    
admin.site.register(Customer, CustomerAdmin)

class TxnnAdmin(admin.ModelAdmin):
    list_display    = ('user_id', 'amount', 'type', 'narration', 'date', 'time')
    search_fields   = ('date', 'type')
    readonly_fields = ()
    
admin.site.register(Txnn, TxnnAdmin)