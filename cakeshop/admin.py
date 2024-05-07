from django.contrib import admin
from cakeshop.models import Category,Occasion,Flavour,Cake,CakeVariant,Order,OrderItems
# Register your models here.
admin.site.register(Category)
admin.site.register(Occasion)
admin.site.register(Flavour)
admin.site.register(Cake)
admin.site.register(CakeVariant)
admin.site.register(Order)
admin.site.register(OrderItems)
