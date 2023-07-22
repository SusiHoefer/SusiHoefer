from django.contrib import admin
from . models import * #imports every model from current location
# Register your models here.

admin.site.register(Customer) #registers the models to the admin-site to show them there
admin.site.register(Article)
admin.site.register(Order)
admin.site.register(OrderedArticle)
admin.site.register(Adress)


