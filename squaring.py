from math import isqrt

def create_square_grid(number):
    # Calculate the square root of the number
    square_root = isqrt(number)

    # Convert the square root to a string for processing
    square_root_str = str(square_root)

    # Determine the number of digits in the square root
    num_digits = len(square_root_str)

    # Pad the original number with zeros if necessary
    number_str = str(number).zfill(num_digits**2)

    # Create the square grid
    grid = [[int(number_str[i*num_digits + j]) for j in range(num_digits)] for i in range(num_digits)]

    return grid

# Test cases
print(create_square_grid(123456789))
print(create_square_grid(1234567891))
