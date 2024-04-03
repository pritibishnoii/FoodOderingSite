from django.contrib import admin
from .models.Product import Product
from .models.category import Category
from .models.scustomer import SCustomer
from .models.orders import Order


# to show fields actual label in Admin site view
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminOreder(admin.ModelAdmin):
    list_display = ['customer','price','product']


'''
class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone','password']
'''
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order)
admin.site.register(SCustomer)