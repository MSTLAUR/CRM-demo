from django.contrib import admin
from .models import Item, newProductModels


# Register your models here.


admin.site.site_header = "NU SCHOOL WILL  "
admin.site.site_title = "Piano@WILL  "
admin.site.index_title = "welcome back Will "

admin.site.register(Item)
admin.site.register(newProductModels)
