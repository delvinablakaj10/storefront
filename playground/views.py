from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Func, Value, Count, ExpressionWrapper, DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Order, OrderItem, Product
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    content_type=ContentType.objects.get_for_model(Product)
    queryset = TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
        )
    return render(request, "hello.html")
