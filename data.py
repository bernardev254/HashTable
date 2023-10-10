import random
import string

# Function to generate a random name
def generate_name():
    name_length = random.randint(5, 10)  # Random length between 5 and 10 characters
    return ''.join(random.choice(string.ascii_letters) for _ in range(name_length))

# Function to generate a random phone number
def generate_phone_number():
    return ''.join(random.choice(string.digits) for _ in range(10))  # 10-digit phone number
def generate_key_value():
    # Create a list of 100 key-value pairs
    k_vpairs = [(generate_name(), generate_phone_number()) for _ in range(100)]
    return k_vpairs
