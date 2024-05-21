from django.contrib import admin
from .models import Slider
from adminsortable2.admin import SortableAdminMixin
# Register your models here.

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'shown', 'my_order') 
    search_fields = ('name',) 
    list_editable = ('image', 'shown',)
    empty_value_display = '-пусто-'