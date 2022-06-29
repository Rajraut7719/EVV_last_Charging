from django.contrib import admin
from .models import Charger_Management
# Register your models here.
@admin.register(Charger_Management)
class Charger_management_Admin(admin.ModelAdmin):
    list_display=['id','charger_name','city','location','charger_id','charger_photo','on_off']
    list_filter = ('charger_name','charger_id')
    search_fields = ('charger_name','charger_id')
    list_per_page = 10 