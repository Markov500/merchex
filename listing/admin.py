from django.contrib import admin

from listing.models import Band, Listing

# Register your models here.


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('title', 'year', 'sold', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
