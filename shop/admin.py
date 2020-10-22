from django.contrib import admin

from .models import Product,Contact,orders, Orderupdate
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(orders)
admin.site.register( Orderupdate )
# Register your models here.
