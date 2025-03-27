from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_coordinates(address):
    try:
        geolocator = Nominatim(user_agent="blood_donation_geocoder")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None
