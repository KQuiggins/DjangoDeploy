from django.contrib import admin
from .models import Product


admin.site.site_header = "Ken's Tech Shop"
admin.site.site_title = "Tech Shop"
admin.site.index_title = "Welcome to Ken's Tech Shop"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller_name', 'desc')
    list_filter = ('seller_name', 'price')
    search_fields = ('name', 'desc')
    list_per_page = 10

    def set_price_one_hundred(self, request, queryset):
        queryset.update(price=100)

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)

    actions = ('set_price_one_hundred','set_price_to_zero')
    list_editable = ('price', 'desc')



admin.site.register(Product, ProductAdmin)


