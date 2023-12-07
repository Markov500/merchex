# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from listing.forms import BandForm, ListingForm
from .models import Band, Listing


def bands(request):
    bands = Band.objects.all()
    return render(request, "listing/band_list.html",  {'bands': bands})


def band_details(request, band_id: int):
    band = Band.objects.get(id=band_id)
    return render(request, "listing/band_details.html",  {'band': band})


def band_create(request: HttpRequest):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm()
    return render(request, "listing/band_create.html", {"form": form})


def band_update(request: HttpRequest, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listing/band_update.html", {"form": form})


def band_delete(request: HttpRequest, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        band.delete()
        return redirect('bands')
    else:
        form = BandForm(instance=band)
    return render(request, "listing/band_delete.html", {"form": form})


def listings(request):
    listings = Listing.objects.all()
    return render(request, "listing/listing_list.html",  {'listings': listings})


def listing_details(request, id: int):
    listing = Listing.objects.get(id=id)
    return render(request, "listing/listing_details.html",  {'listing': listing})


def listing_create(request: HttpRequest):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing_details', listing.id)
    else:
        form = ListingForm()

    return render(request, "listing/band_create.html", {"form": form})


def listing_update(request: HttpRequest, id):
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        form.save()
        return redirect('listing_details', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, "listing/listing_update.html", {"form": form})


def listing_delete(request: HttpRequest, id):
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        listing.delete()
        return redirect('listings')
    else:
        form = ListingForm(instance=listing)
    return render(request, "listing/listing_delete.html", {"form": form})


def about(request):
    return render(request, "listing/about.html")
