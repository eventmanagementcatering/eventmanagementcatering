from django.contrib import admin
from eventapp.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('firstname','email','subject','message',)

@admin.register(booking)
class bookingadmin(admin.ModelAdmin):
    pass

@admin.register(eventrequest)
class eventrequestadmin(admin.ModelAdmin):
    list_display=('fullname','email','message',)

@admin.register(blogs)
class blogsadmin(admin.ModelAdmin):
    pass
@admin.register(events)
class eventsadmin(admin.ModelAdmin):
    pass
@admin.register(decoration)
class decorationadmin(admin.ModelAdmin):
    pass
@admin.register(menu)
class menuadmin(admin.ModelAdmin):
    pass
@admin.register(FAQs)
class FAQsadmin(admin.ModelAdmin):
    pass
@admin.register(packages)
class packagesadmin(admin.ModelAdmin):
    pass
@admin.register(Vendor)
class Vendoradmin(admin.ModelAdmin):
    pass
@admin.register(Vendordetail)
class Vendordetailadmin(admin.ModelAdmin):
    pass