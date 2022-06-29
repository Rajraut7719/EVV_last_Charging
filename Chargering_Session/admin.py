from django.contrib import admin
from .models import Chargering_Session
# Register your models here.
@admin.register(Chargering_Session)
class Charging_session_Admin(admin.ModelAdmin):
    list_display=['id','customer_name','customer_mobile_no','customer_id', 'city','location','start_date_time','end_date_time','total_time','consume_power']
    list_filter = ('customer_name','customer_mobile_no','customer_id')
    search_fields = ('customer_name','customer_mobile_no','customer_id')
    list_per_page = 10 