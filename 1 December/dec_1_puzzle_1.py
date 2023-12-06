"""
Project:        Advent of Code, 2023
Puzzle Date:    1 December
Author:         Shane Taggart
Author Date:    5 December, 2023
Details:        The solution for puzzle one, part one.

Puzzle:         You try to ask why they can't just use a weather machine ("not powerful enough")
                and where they're even sending you ("the sky") and why your map looks mostly blank
                ("you sure ask a lot of questions") and hang on did you just say the sky ("of
                course, where do you think snow comes from") when you realize that the Elves
                are already loading you into a trebuchet ("please hold still, we need
                to strap you in").

                As they're making the final adjustments, they discover that their calibration
                document (your puzzle input) has been amended by a very young Elf who was apparently
                just excited to show off her art skills. Consequently, the Elves are having trouble
                reading the values on thedocument.

                The newly-improved calibration document consists of lines of text; each line
                originally contained a specific calibration value that the Elves now need to
                recover. On each line, the calibration value can be found by combining the
                first digit and the last digit (in that order) to form a single two-digit number.

                For example:

                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet

                In this example, the calibration values of these four lines are 12, 38, 15, and 77.
                Adding these together produces 142.

                Consider your entire calibration document.
                What is the sum of all of the calibration values?
"""

import dec_1_puzzle_input

def extract_coordinates(messy_coords_string):
    """
    extract_coordinates( String|messy_coords ): Integer|coords_sum

    This function takes the provided String and returns the sum of the first and last numeral
    found in each line of the provided String.
    

    Parameters:

    String|messy_coords - A String containing 1 or more lines. Each line may contain letters
    and numerals.
    
    
    Return Value(s):
    
    Integer|coords_sum - An Integer containing the sum of all numbers found by parsing the String.

    """

    # Convert the provided String into an Array, each item separated by a carriage return.
    messy_coords_array = messy_coords_string.split("\n")
    
    # Create empty Arrays to store the coordinates at various stages of parsing.
    clean_coords_array = []
    individual_coords = []

    # Iterate over each line in the Array.
    for line in messy_coords_array:
        # Create/reset the String, which will store the numerals found in the current line.
        numerals_in_line = ""
        # Iterate over every character inside of each line in the Array.
        for char in line:
            # Conditional to check if the current character is a digit.
            if char.isdigit():
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
