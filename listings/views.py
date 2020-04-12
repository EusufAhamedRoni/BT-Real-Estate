from django.shortcuts import render

def listingsView(request):
    template = 'listings/listings.html'

    return render(request, template)

def listingView(request):
    template = 'listings/listing.html'

    return render(request, template)

def searchView(request):
    template = 'listings/search.html'

    return render(request, template)
