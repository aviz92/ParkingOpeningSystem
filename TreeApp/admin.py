from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.conf import settings

from .models import LeveledTree, Categories, Parameters, ParametersTree


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')

    list_display_links = ('id', 'category_name', 'description')

    search_fields = ('category_name', 'description')

    list_editable = ()

    list_filter = ('id', 'category_name', 'description')

    fields = ('category_name', 'description')

    readonly_fields = ('id', )

    save_on_top = True


class ParametersAdmin(admin.ModelAdmin):
    list_display = ('id', 'variable_name', 'variable_category', 'description')

    list_display_links = ('id', 'variable_name', 'variable_category', 'description')

    search_fields = ('variable_name', 'variable_category', 'description')

    list_editable = ()

    list_filter = ('id', 'variable_name', 'variable_category', 'description')

    fields = ('variable_name', 'variable_category', 'description')

    readonly_fields = ('id', )

    save_on_top = True


class ParametersTreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'variable_name', 'variable_value', 'fk', 'description')

    list_display_links = ('id', 'variable_name', 'variable_value', 'fk', 'description')

    search_fields = ('variable_name', 'variable_value', 'fk', 'description')

    list_editable = ()

    list_filter = ('id', 'variable_name', 'variable_value', 'fk', 'description')

    fields = ('variable_name', 'variable_value', 'fk', 'description')

    readonly_fields = ('id', )

    save_on_top = True


class ParametersTreeInline(admin.TabularInline):
    model = ParametersTree
    verbose_name_plural = "My Parameters"
    verbose_name = "Parameters"
    extra = 0


class LeveledTreeAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('id', 'name', 'apartment_number', 'description', 'parent')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_tree_animation_speed(self):
        return 0 if getattr(settings, "DJANGO_TESTING", False) else None

    def get_tree_mouse_delay(self):
        return 0 if getattr(settings, "DJANGO_TESTING", False) else None

    inlines = [ParametersTreeInline]


admin.site.register(LeveledTree, LeveledTreeAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Parameters, ParametersAdmin)
admin.site.register(ParametersTree, ParametersTreeAdmin)
