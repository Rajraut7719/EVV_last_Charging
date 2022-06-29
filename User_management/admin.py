from django.contrib import admin
from .models import User

@admin.register(User)
class User_management_Admin(admin.ModelAdmin):
    list_display=['id','username','full_name','mobile','email']
    list_filter = ('username','mobile')
    search_fields = ('username','mobile')
    list_per_page = 10 

