from django.contrib import admin
from .models import ApartmentNumber


class ApartmentNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'apartment_number', 'created_at', 'updated_at', 'en_dis')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_editable = ()

    list_filter = ('en_dis', 'created_at', 'updated_at', 'name', 'description', 'apartment_number', 'parking_count')

    fields = ('en_dis', 'created_at', 'updated_at', 'name', 'description', 'apartment_number', 'parking_number', 'parking_count',
              'amount_of_parking')

    readonly_fields = ('id', 'created_at', 'updated_at', 'parking_count', 'amount_of_parking')

    @staticmethod
    def amount_of_parking(obj):
        if obj.get_amount_of_parking:
            return obj.get_amount_of_parking()
        else:
            return '-'

    save_on_top = True


admin.site.register(ApartmentNumber, ApartmentNumberAdmin)
