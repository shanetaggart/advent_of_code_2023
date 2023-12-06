"""
Project:        Advent of Code, 2023
Puzzle Date:    1 December
Author:         Shane Taggart
Author Date:    6 December, 2023
Details:        The solution for puzzle two, part one.
"""

import dec_2_puzzle_input

def sum_of_ids(games):

    games = games.split("\n")

    for line in games:
        print(line)
    return

if __name__ == "__main__":
    # Print the example output to the CLI.
    EXAMPLE_OUTPUT = sum_of_ids(dec_2_puzzle_input.EXAMPLE_INPUT)
    example_fstring = f"Example Puzzle Input Result: {EXAMPLE_OUTPUT}"
    print(example_fstring)

    # Print the puzzle output to the CLI
    # PUZZLE_OUTPUT = sum_of_ids(dec_2_puzzle_input.PUZZLE_INPUT)
    # puzzle_fstring = f"Puzzle Input Result: {PUZZLE_OUTPUT}"
    # print(puzzle_fstring)