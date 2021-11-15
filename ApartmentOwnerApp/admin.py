from django.contrib import admin

from .models import ApartmentOwner

from ApartmentNumberApp.models import ApartmentNumberApartmentOwner
from CarNumberApp.models import CarNumberApartmentOwner
from MotorcycleNumberApp.models import MotorcycleNumberApartmentOwner


class ApartmentNumberApartmentOwnerInline(admin.TabularInline):
    model = ApartmentNumberApartmentOwner
    verbose_name_plural = "My Apartment"
    verbose_name = "Apartment Number"
    extra = 0


class CarNumberApartmentOwnerInline(admin.TabularInline):
    model = CarNumberApartmentOwner
    verbose_name_plural = "My Cars"
    verbose_name = "Car Number"
    extra = 0


class MotorcycleNumberApartmentOwnerInline(admin.TabularInline):
    model = MotorcycleNumberApartmentOwner
    verbose_name_plural = "My Motorcycles"
    verbose_name = "Motorcycle Number"
    extra = 0


class ApartmentOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'en_dis')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_editable = ()

    list_filter = ('en_dis', 'created_at', 'updated_at', 'name', 'description')

    fields = ('en_dis', 'created_at', 'updated_at', 'name', 'description')

    readonly_fields = ('id', 'created_at', 'updated_at')

    save_on_top = True

    inlines = [ApartmentNumberApartmentOwnerInline, CarNumberApartmentOwnerInline, MotorcycleNumberApartmentOwnerInline]


admin.site.register(ApartmentOwner, ApartmentOwnerAdmin)
