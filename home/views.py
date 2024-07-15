import math

import requests
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import quote
from .models import TravelDestination


def index(request):
    return render(request, "home/index.html", {})


def fetch_destinations(request, page):
    # page = int(request.GET.get('page', 1))
    limit = 30
    offset = (page - 1) * limit

    # check if records are in cache database
    saved_record_count = TravelDestination.objects.all().count()

    # fill data if not sufficient
    if saved_record_count < 50:
        fetch_and_save_destinations()

    # get data from cache database
    stored_records = TravelDestination.objects.all()

    page_data = stored_records[offset:offset + limit]
    total_pages = math.ceil(saved_record_count / limit)

    return render(request, 'home/explore.html', {'destinations': page_data, 'curr_page': page, "total_pages": total_pages})


def fetch_and_save_destinations(offset=0, limit=50):
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
