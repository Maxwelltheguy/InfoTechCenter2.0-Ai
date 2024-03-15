import random
from time import sleep

GAS_LEVELS = {
    "Empty": 0,
    "Low": 10,
    "Quarter Tank": 25,
    "Half Tank": 50,
    "Three Quarter Tank": 75,
    "Full Tank": 100
}

GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]


def gas_level_gauge():
    return random.choices(list(GAS_LEVELS.keys()), weights=GAS_LEVELS.values())[0]


def list_of_gas_stations():
    return random.choice(GAS_STATIONS)


def gas_level_alert():
    gas_level = gas_level_gauge()

    if gas_level == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***")
        sleep(1.25)
        print("\n    *** Calling Triple AAA ***")
    elif gas_level == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(2.25)
        print(f"The closest gas station is {list_of_gas_stations()} which is {random.uniform(1, 25):.1f} miles away.")
    elif gas_level == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station.")
        sleep(2.25)
        print(
            f"The closest gas station is {list_of_gas_stations()} which is {random.uniform(25.1, 50):.1f} miles away.")
    elif gas_level == "Half Tank":
        print("Your gas tank is halfway full which is plenty to get to your destination.")
    elif gas_level == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full.")


gas_level_alert()
