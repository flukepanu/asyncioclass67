# Synchronous cooking
# Kitchen 1, 1 chef, 1 dish

import time
from time import sleep, ctime

# Cooking synchronous
def cooking(index):
    print(f'{ctime()} Kitchen-{index}: Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index}: Cooking done!')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main: Start Cooking.')
    start_time = time()

    # Cooking
    cooking(0)

    duration = time() - start_time
    print(f'{ctime()} Main: Finished Cooking duration in {(duration):0.2f} seconds')

