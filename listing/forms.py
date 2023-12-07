from django import forms

from listing.models import Band, Listing


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__'
        exclude = ("active", "official_homepage")


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__'
        exclude = ('sold',)
