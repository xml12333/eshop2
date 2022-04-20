from django.contrib import admin
from .models import Product, Variation,ReviewRating,ProductGallery
import admin_thumbnails 

@admin_thumbnails.thumbnail('image', 'Thumbnail')
class ProductGallaryInline(admin.TabularInline):
    model = ProductGallery
    extra=1

class PruductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name', 'price','stock','category','modified_date','is_available')
    inlines = [ProductGallaryInline]

class VariationAdmin(admin.ModelAdmin):
        list_display = ('product', 'variation_category','variation_value','is_active')
        list_editable = ('is_active',)
        list_filter = ('product', 'variation_category','variation_value','is_active')


admin.site.register(Product,PruductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
