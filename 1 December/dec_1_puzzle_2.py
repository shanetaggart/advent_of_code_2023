"""
Project:        Advent of Code, 2023
Puzzle Date:    1 December
Author:         Shane Taggart
Author Date:    5 December, 2023
Details:        The solution for puzzle one, part two.

Puzzle:         Your calculation isn't quite right. It looks like some of the digits are
                actually spelled out with letters: one, two, three, four, five, six, seven,
                eight, and nine also count as valid "digits".

                Equipped with this new information, you now need to find the real first
                and last digit on each line. For example:

                two1nine
                eightwothree
                abcone2threexyz
                xtwone3four
                4nineeightseven2
                zoneight234
                7pqrstsixteen

                In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
                Adding these together produces 281.

                What is the sum of all of the calibration values?
"""

import dec_1_puzzle_input

def extract_coordinates(messy_coords_string):
    """
    extract_coordinates( String|messy_coords ): Integer|coords_sum

    This function takes the provided String and returns the sum of the first and last numbers
    found in each line of the provided String. A number is categorized as either:

    - A numeral (example: 1, 5, 6, 7)
    - A String representing a numeral (example: 'two', 'three', 'eight', 'nine')
    

    Parameters:

    String|messy_coords - A String containing 1 or more lines. Each line may contain letters
    and numerals.
    
    
    Return Value(s):
    
    Integer|coords_sum - An Integer containing the sum of all numbers found by parsing the String.

    """

    # Store the String versions of all ten singular digits.
    string_numerals = [
        ["zero", "0"],
        ["one", "1"],
        ["two", "2"],
        ["three", "3"],
        ["four", "4"],
        ["five", "5"],
        ["six", "6"],
        ["seven", "7"],
        ["eight", "8"],
        ["nine", "9"]
    ]

    # Iterate over all of the string numerals and replace the string versions with numerals.
    for key, value in enumerate(string_numerals):
        messy_coords_string = messy_coords_string.replace(value[0], value[1])

    # Convert the provided String into an Array, each item separated by a carriage return.
    messy_coords_array = messy_coords_string.split("\n")
    print(messy_coords_array)
    
    # Create empty Arrays to store the coordinates at various stages of parsing.
    clean_coords_array = []
    individual_coords = []

    # Iterate over each line in the Array.
    for line in messy_coords_array:
        # Create/reset the String, which will store the numerals found in the current line.
        numerals_in_line = ""
        # Iterate over every character inside of each line in the Array.
        for char in line:
            # Conditional to check if the current character is a numeral.
            if char.isnumeric():
                # When the current character is a numeral, append it to the String.
                numerals_in_line += char
        # When the current Iteration have finished parsing, append the numerals to the Array.
        clean_coords_array.append(numerals_in_line)

    # Iterate over every coordinate inside of the Array.
    for coord in clean_coords_array:
        # Ensure that the current coordinate is not empty.
        if coord != "":
            # Store the first and last numeral.
            new_coord = coord[0] + coord[-1]
            # Append the new coordinate to the Array.
            individual_coords.append(int(new_coord))

    # Store the sum of all of the coordinates in the Array, and return it.
    coords_sum = sum(individual_coords)
    return coords_sum

if __name__ == "__main__":
    # Store the results of the function for easy formatting.
    example_output = extract_coordinates(dec_1_puzzle_input.EXAMPLE_INPUT)
    puzzle_output = extract_coordinates(dec_1_puzzle_input.PUZZLE_INPUT)

    # Create format strings for CLI output.
    example_fstring = f"Example Puzzle Input Result: {example_output}"
    puzzle_fstring = f"Puzzle Input Result: {puzzle_output}"

    # Print the result to the CLI.
    print(example_fstring + "\n" + puzzle_fstring)
