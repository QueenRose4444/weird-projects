import time
import random

def generate_random_data(size):
    return bytearray(random.getrandbits(8) for _ in range(size))

data = []

while True:
    data.append(generate_random_data(1024 * 1024))  # Append 1MB of random data
    time.sleep(1)
