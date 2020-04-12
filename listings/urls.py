from django.urls import path
from .import views

app_name = 'listings'

urlpatterns = [
    path('', views.listingsView, name='listingsView'),
    path('<int:listing_id>', views.listingView, name='listingView'),
    path('search', views.searchView, name='searchView'),
]
