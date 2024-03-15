import time
import sys

# Constants
LOADING_CYCLES = 20
ELLIPSIS_LIMIT = 4

def print_message(message):
    """Prints a message and flushes the output."""
    sys.stdout.write("\r" + message)
    sys.stdout.flush()

def print_loading_animation():
    """Prints the loading animation."""
    for cycle in range(LOADING_CYCLES):
        ellipsis_count = cycle % (ELLIPSIS_LIMIT + 1)
        message = f"InfoTech Center Operating System Loading{'.' * ellipsis_count}"
        print_message(message)
        time.sleep(0.5)

def main():
    """Main function to run the program."""
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(2)
    print_loading_animation()
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    main()
