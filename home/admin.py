from django.contrib import admin
from home.models import (CategoryModel,
                         ProductModel,
                         BannerModel,
                         GoldPrice)
from django.contrib.auth.models import (User,
                                        Group)


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(CategoryModel)
admin.site.register(ProductModel)


class BannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """Prevent adding new Banner instances"""
        return False  

    def has_delete_permission(self, request, obj=None):
        """Prevent deleting Banner instances"""
        return False 
admin.site.register(BannerModel, BannerAdmin)


class GoldPriceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """Prevent adding new GoldPrice instances"""
        return False  

    def has_delete_permission(self, request, obj=None):
        """Prevent deleting GoldPrice instances"""
        return False 
admin.site.register(GoldPrice, GoldPriceAdmin)