# Import the sleep function.
from time import sleep

# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

# Print each name 5 times.
for name in names:
    # Pause for 1 second between batches, and then skip two lines.
    sleep(1)
    print("\n\n")
    
    for x in range(0,5):
        print(name.title())