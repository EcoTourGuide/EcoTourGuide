import math

import requests
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from urllib.parse import quote
from django.contrib import messages
from .forms import ContactForm
from .models import TravelDestination, ContactMessage


def index(request):
    return render(request, "home/index.html", {})


def fetch_destinations(request, page):
    # page = int(request.GET.get('page', 1))
    limit = 30
    offset = (page - 1) * limit

    # Check if records are in cache database
    saved_record_count = TravelDestination.objects.all().count()

    # Fill data if not sufficient
    if saved_record_count < 50:
        fetch_and_save_destinations()

    # Get filter parameters
    palm_level = request.GET.get('palm_level')
    lodge_type = request.GET.get('lodge_type')
    city = request.GET.get('city')
    phy_addr = request.GET.get('phy_addr')

    # Apply filters
    filters = {}
    if palm_level:
        filters['palm_level'] = palm_level
    if lodge_type:
        filters['lodge_type'] = lodge_type
    if city:
        filters['city__icontains'] = city
    if phy_addr:
        filters['phy_addr__icontains'] = phy_addr

    # Debug output
    print(f"Filters: {filters}")

    # Get data from cache database
    stored_records = TravelDestination.objects.filter(**filters)

    page_data = stored_records[offset:offset + limit]
    total_pages = math.ceil(stored_records.count() / limit)

    return render(request, 'home/explore.html', {'destinations': page_data, 'curr_page': page, "total_pages": total_pages})

def fetch_and_save_destinations(offset=0, limit=10):
    encoded_out_fields = quote('*')

    api_url = (f"https://ca.dep.state.fl.us/arcgis/rest/services/OpenData/OSI_DATA/MapServer/0/query?where=1%3D1"
               f"&outFields={encoded_out_fields}&outSR=4326&f=json&resultOffset={offset}&resultRecordCount={limit}")

    # Fetch data from the API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        features = data.get('features', [])  # Get the features from the response

        # Create a list to hold TravelDestination instances
        travel_destinations = []

        for feature in features:
            attributes = feature.get('attributes', {})
            geometry = feature.get('geometry', {})

            # Create a TravelDestination instance
            travel_destination = TravelDestination(
                designation_num=attributes.get('DESIGNATIONNUM'),
                county=attributes.get('COUNTY'),
                prop_name=attributes.get('PROPNAME'),
                phy_addr=attributes.get('PHYADDR'),
                city=attributes.get('CITY'),
                zip_code=attributes.get('ZIP'),
                phone=attributes.get('PHONE'),
                web=attributes.get('WEB'),
                lodge_type=attributes.get('LODGETYPE'),
                palm_level=attributes.get('PALMLEVEL'),
                latitude=attributes.get('LATITUDE'),
                longitude=attributes.get('LONGITUDE')
            )

            # Add the instance to the list
            travel_destinations.append(travel_destination)

        try:
            count = TravelDestination.objects.bulk_create(travel_destinations).count()
            return count
        except Exception as e:
            print("Error during database operation:", e)
            return -1

    else:
        print("Failed to fetch data from the API. Status code:", response.status_code)
        return -1

###############JIDNESH###############
def support(request):
    return render(request, 'home/support.html')
def contact_us(request):
    return render(request, 'home/contact_us.html')

def terms_policies(request):
    return render(request, 'home/terms_policies.html')

def details(request, destination_id):
    destination = TravelDestination.objects.get(pk=destination_id)
    destination_details = TravelDestinationDetails.objects.get(pk=destination_id)
    reviews = Review.objects.filter(reviewed_facility__object_id=destination_id)

    # calculating avg rating
    avg = reviews.aggregate(Avg('rating'))['rating__avg']
    print("avg is: ", avg)
    average_rating = 0 if avg is None else math.floor(avg)

    # getting nearby destinations
    all_destinations = TravelDestination.objects.all()
    nearby_destinations = TravelDestination.objects.filter(city=destination.city)

    context = {
        'destination': destination,
        'destination_details': destination_details,
        'palm_rating_range': range(int(destination.palm_level)),
        'average_rating': average_rating,
        'total_reviews': reviews.count(),
        'nearby_destinations': nearby_destinations,
        'reviews': reviews
    }

    return render(request, "home/details.html", context)



def aboutus(request):
    return render(request, 'home/aboutus.html')





# contact/views.py


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'home/contactus.html', {'form': form})


