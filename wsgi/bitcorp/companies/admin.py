from django.contrib import admin

from .models import company, investment

admin.site.register(company)
admin.site.register(investment)
