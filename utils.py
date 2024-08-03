import pandas as pd
from math import radians, cos, sin, sqrt, atan2


# Function to calculate distance between two points using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def find_nearby_hotels(lat, long, radius, rating=0):
    # Load the dataset
    hotels = pd.read_csv('Hotels_List.csv')

    # Calculate distances
    hotels['Distance'] = hotels.apply(lambda row: haversine(lat, long, row['Latitude'], row['Longitude']), axis=1)

    # Filter hotels based on distance and optional minimum rating
    nearby_hotels = hotels[(hotels['Distance'] <= radius) & (hotels['Rating'] >= rating)]
    return nearby_hotels
