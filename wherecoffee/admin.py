from django.contrib import admin
from .models import Order, Coffee
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('nicker', 'location',"tel","licence")
    search_fields = ('nicker',"tel",)
    date_hierarchy = 'create_time'

admin.site.register(Coffee)
admin.site.register(Order, OrderAdmin)
