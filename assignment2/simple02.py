# Synchronous cooking

# Import the time module
from time import sleep, ctime, time

# Define the cooking function
def cooking(index):
    # Print the start message
    print(f'{ctime()} Kitchen-{index}: Begin cooking...')

    # Simulate cooking by sleeping for 2 seconds
    sleep(2)

    # Print the completion message
    print(f'{ctime()} Kitchen-{index}: Cooking done!')

# Begin the main thread
if __name__ == "__main__":
    # Print the start message
    print(f'{ctime()} Main: Start Cooking.')

    # Start the timer
    start_time = time()

    # Cook each dish
    for index in range(2):
        cooking(index)

    # End the timer
    duration = time() - start_time

    # Print the completion message
    print(f'{ctime()} Main: Finished Cooking. Duration: {duration:.2f} seconds')
