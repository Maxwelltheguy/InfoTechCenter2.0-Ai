# Import necessary libraries
import time
import sys

# Set the duration for initial sleep
timeToSleep = 2

# Print welcome message
print("\n\nWelcome to InfoTech Center V1.0\n")

# Sleep for the specified duration
time.sleep(timeToSleep)

# Initialize variables for the loading animation
x = 0
ellipsis = 0

# Loop to simulate loading animation
while x != 20:
    # Increment cycle count
    x += 1
    # Construct loading message with ellipsis
    message = ("InfoTech Center Operating System Loading" + "." * ellipsis)
    # Increment ellipsis count
    ellipsis += 1
    # Print loading message with carriage return to overwrite previous output
    sys.stdout.write("\r" + message)
    # Wait for 0.5 seconds
    time.sleep(.5)
    # Reset ellipsis count after reaching the limit
    if ellipsis == 4:
        ellipsis = 0
    # Print booted message after completing 20 cycles
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")
