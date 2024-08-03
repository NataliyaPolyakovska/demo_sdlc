# This is a sample Python script.

from utils import find_nearby_hotels


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lat = 50.1109
    long = 8.6821
    radius = 0.2  # kilometers

    result = find_nearby_hotels(lat, long, radius)
    print(result)

