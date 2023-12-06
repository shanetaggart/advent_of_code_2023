"""
Project:        Advent of Code, 2023
Puzzle Date:    1 December
Author:         Shane Taggart
Author Date:    5 December, 2023
Details:        The solution for puzzle one, part one.
"""

import dec_1_puzzle_input

def extract_coordinates(messy_coords_string):
    """
    extract_coordinates( String|messy_coords ): Integer|coords_sum

    This function takes the provided String and returns the sum of the first and last digit
    found in each line of the provided String.
    

    Parameters:

    String|messy_coords - A String containing 1 or more lines. Each line may contain letters
    and digits.
    
    
    Return Value(s):
    
    Integer|coords_sum - An Integer containing the sum of all numbers found by parsing the String.

    """

    # Convert the provided String to an Array by separating by a carriage return.
    messy_coords_array = messy_coords_string.split("\n")
    
    # Instantiate an empty integer to store the sum of the coordinates.
    coords_sum = int()
    
    # Iterate over each line in the Array.
    for line in messy_coords_array:
        # Create a temporary Array to hold the digits found in the current line.
        digits_in_line = []
        # Iterate over every character in the current line.
        for char in line:
            # Check if the current character is a digit.
            if char.isdigit():
                # If it is a digit, append that digit to the Array
                digits_in_line.append(char)
        # Convert the first and last digits to Integers and add them to the sum.
        coords_sum += int(digits_in_line[0] + digits_in_line[-1])
    # Return the sum after iterating over all Array items.
    return coords_sum

if __name__ == "__main__":
    # Print the example output to the CLI.
    EXAMPLE_OUTPUT = extract_coordinates(dec_1_puzzle_input.EXAMPLE_INPUT)
    example_fstring = f"Example Puzzle Input Result: {EXAMPLE_OUTPUT}"
    print(example_fstring)

    # Print the puzzle output to the CLI
    PUZZLE_OUTPUT = extract_coordinates(dec_1_puzzle_input.PUZZLE_INPUT)
    puzzle_fstring = f"Puzzle Input Result: {PUZZLE_OUTPUT}"
    print(puzzle_fstring)
