from django.contrib import admin

from medicine.portal.models import Pill, Category

# Register your models here.


admin.site.register(Pill)

admin.site.register(Category)