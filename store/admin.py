from collections import Counter
from django.contrib import admin
from . import models
from django.db.models import Count


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    #fields=['title', 'slug']
    list_display=['title', 'unit_price', 'collection']
    list_editable=['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    search_fields=['title__istartswith']
    list_filter = ['collection']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name','membership']
    list_editable=['membership']
    list_per_page = 10



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'placed_at', 'customer']
    list_per_page = 10


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))


