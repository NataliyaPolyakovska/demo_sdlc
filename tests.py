import unittest
from utils import find_nearby_hotels, haversine


class TestStringMethods(unittest.TestCase):
    def test_distance_calculation(self):
        # Coordinates of New York (latitude: 40.7128, longitude: -74.0060)
        # and Los Angeles (latitude: 34.0522, longitude: -118.2437)
        # Known distance is approximately 3940 kilometers
        lat1, lon1 = 40.7128, -74.0060
        lat2, lon2 = 34.0522, -118.2437
        distance = haversine(lat1, lon1, lat2, lon2)
        # Test if the calculated distance is within a reasonable error margin
        self.assertAlmostEqual(distance, 3940, delta=100)  # Allowing a delta for approximation

    def test_find_nearby_hotels(self):
        # This test remains the same to ensure backward compatibility
        assert find_nearby_hotels(50.1109, 8.6821, 0.3)['Hotel Name'].iloc[0] == 'Mandarin Oriental'

    def test_find_nearby_hotels_empty(self):
        # This test remains the same to ensure backward compatibility
        assert len(find_nearby_hotels(50.1109, 8.6821, 0)) < 1



if __name__ == '__main__':
    unittest.main()

