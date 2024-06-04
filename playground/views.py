from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import (Count, DecimalField, ExpressionWrapper, F, Func,
                              Value)
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Order, OrderItem, Product
from tags.models import TaggedItem


@transaction.atomic()
def say_hello(request):
    # TaggedItem.objects.get_tags_for(Product,1)
    order = Order()
    order.customer_id=1
    order.save()

    item=OrderItem()
    item.order = order
    item.product_id=1
    item.quantity=1
    item.unit_price=10
    item.save()
   
    return render(request, "hello.html")
