from django.contrib import admin
from .models import Client, User, Entry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Entry)





# Config del panel
title = "Proyecto INQUIMEP"
subtitle = "Panel de gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle