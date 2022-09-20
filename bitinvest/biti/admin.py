from django.contrib import admin

from biti import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Trade)
admin.site.register(models.KGS)
admin.site.register(models.Invest)
admin.site.register(models.InvestmentCountries)
admin.site.register(models.Settings)