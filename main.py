# This is a sample Python script.

from utils import find_nearby_hotels


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    result = find_nearby_hotels(50.1109, 8.6821, 0.3)['Hotel Name'].iloc[0]
    print(result)

