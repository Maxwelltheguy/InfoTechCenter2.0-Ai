import random
from time import sleep

# Dictionary to represent gas levels and their associated percentages
GAS_LEVELS = {
    "Empty": 0,
    "Low": 10,
    "Quarter Tank": 25,
    "Half Tank": 50,
    "Three Quarter Tank": 75,
    "Full Tank": 100
}

# List of gas station names
GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]


# Function to randomly select a gas level based on the percentages defined in GAS_LEVELS
def gas_level_gauge():
    return random.choices(list(GAS_LEVELS.keys()), weights=GAS_LEVELS.values())[0]


# Function to randomly select a gas station from the GAS_STATIONS list
def list_of_gas_stations():
    return random.choice(GAS_STATIONS)


# Function to alert the user based on their gas level
def gas_level_alert():
    gas_level = gas_level_gauge()

    if gas_level == "Empty":
        # Warning message if gas level is empty
        print("*** WARNING - YOU ARE ON EMPTY ***")
        sleep(1.25)  # Sleeping for dramatic effect
        print("\n    *** Calling Triple AAA ***")
    elif gas_level == "Low":
        # Alert message for extremely low gas level, along with the closest gas station
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(2.25)  # Sleeping to simulate searching time
        print(f"The closest gas station is {list_of_gas_stations()} which is {random.uniform(1, 25):.1f} miles away.")
    elif gas_level == "Quarter Tank":
        # Alert message for quarter tank gas level, along with the closest gas station
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station.")
        sleep(2.25)  # Sleeping to simulate searching time
        print(
            f"The closest gas station is {list_of_gas_stations()} which is {random.uniform(25.1, 50):.1f} miles away.")
    elif gas_level == "Half Tank":
        # Informative message for half tank gas level
        print("Your gas tank is halfway full which is plenty to get to your destination.")
    elif gas_level == "Three Quarter Tank":
        # Informative message for three quarter tank gas level
        print("Your gas tank is at three quarter tank.")
    else:
        # Informative message for full tank gas level
        print("Your gas tank is full.")


# Calling the gas_level_alert function to simulate gas level alerts
gas_level_alert()
