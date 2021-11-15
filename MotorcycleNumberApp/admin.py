from django.contrib import admin
from .models import MotorcycleNumber


class MotorcycleNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'motorcycle_number', 'created_at', 'updated_at', 'en_dis')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_editable = ()

    list_filter = ('en_dis', 'created_at', 'updated_at', 'name', 'description', 'motorcycle_number')

    fields = ('en_dis', 'created_at', 'updated_at', 'name', 'description', 'motorcycle_number')

    readonly_fields = ('id', 'created_at', 'updated_at')

    save_on_top = True


admin.site.register(MotorcycleNumber, MotorcycleNumberAdmin)
