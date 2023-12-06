<style>
    body {
        font-family: 'Lato', sans-serif;
    }

    span {
        font-size: 1.5rem;
        display: block;
    }

    span::before,
    summary::before {
        padding: 0 0.5em 0 0;
    }

    .complete::before {
        content: '\2705';
    }
    
    .work-in-progress::before {
        content: '\1F6A7';
    }

    .puzzle::before {
        content: '\1F9E9';
    }

    .thoughts::before {
        content: '\1F9E0';
    }

    summary {
        font-size: 1.5rem;
        text-transform: uppercase;
        cursor: pointer;
        transition: opacity 0.25s ease;
    }

    summary:hover {
        opacity: 0.7;
    }

</style>

# 1 December, 2023

<span class="complete">Complete</span>

<details>
<summary class="puzzle">Puzzle Details</summary>

**Part 1:**

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on thedocument.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `142`.

Consider your entire calibration document. What is the sum of all of the calibration values?

**Part 2:**

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces `281`.

What is the sum of all of the calibration values?

</details>

<details open>
<summary class="thoughts">Thought Process</summary>

**Part 1**

For part 1 my immediate thought was: "This is just string manipulation, so this should be easy!"

I was mostly right, but ran into a roadblock during part 2, but more on that later.

I started by creating the constants in `dec_1_puzzle_input.py`, and ensuring that I could create an array out of the multiline string.

Once I had the string converted to an array, I iterated over the array with a `for in` loop to ensure there weren't any issues, testing with `print()` at each step.

Once I knew I had the lines, I created a second `for in` loop to iterate over every character inside of each line. I know nested loops are not very performant, however I couldn't think of a better way to accomplish this as every single character needs to be parsed individually.

I knew about Python's `isnumeric()` function which I had originally used to check if the current character was a numeral. Through testing and research I discovered that there's a second function, `isdigit()` that accomplishes the same task for the purposes of this puzzle. The key point being that I learned that `isnumeric()` checks for other kinds of numerals such as roman numerals, which didn't affect this puzzle, however wouldn't be the appropriate way forward if this was to be used for something else. `isdigit()` simply checks if it's a digit, and only a digit, which is a better choice if this were to be used again.

Now the program was confirming what characters were digits, but not doing anything with them. So I created a scoped array to store the digits that it found, only during the inner loop. Once that inner loop was complete, I took the first and last digits by using the indecies `0` and `-1` for first and last respectively. This gave me the digits required per line, but I needed to get the sum of those digits by the end of the program.

At first I created some empty arrays to hold this information as I went through, but eventually settled on not storing the digits, and simply adding them to the sum as the loops progressed, since the digits weren't needed after they were added to the sum.

**Part 2**

Part 2 introduced the problem of having numbers represented in their text form, such as `one`, `five`, etc.

I started by creating a 3D array containing the numbers and their numeral counterparts as strings, much like the following example:

```
string_numerals = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"]
]
```

This wasn't what I settled on in the end, but I had originally thought I could search through the input string, find the text in each subarray at index `0`, and then replace it with the string in that subarray at index `1`.

As I tested this out, I discovered my solution to part 1 wasn't quite positioned in the best way. There were several extra loops and arrays that were unnecessary and causing problems. This is where I refactored the solution for part 1 to it's current state.

Now that the solution for part 1 was much better, I tried replacing the text inside of the input string with the numeral counterparts, interating over the array starting with `one` and ending with `nine`, but my solution wasn't right. I got stuck here for a while, and tried looking for hints from other who were working on the same puzzle.

While looking for hints, I found two things:

- The reson my solution was wrong, was because some of the lines had text like `eightwo` which _should_ have been converted to `8wo`, not `eigh2`. Because I was iterating over all of the lines in the string, and doing so in an order, I was sabotaging myself.

- I also learned that I could use `enumerate()` inside of a `for in` loop to eliminate the need for the 3D array.

Now with a clean 2D array of the string versions of the numerals, I converted the original inner loop to use `enumerate()`, added a second inner loop which also used `enumerate()`, and was able to use the slice operator to compare where I was inside of any given line, against the numbers inside of `string_numerals`. When it found a match, instead of changing it in the string like I did earlier, I simply added it to a scoped array to keep track of all numbers I found inside of that line.

Once a line was fully parsed, I added the first and last digit inside of the scoped array to the sum, and my solution worked!

</details>
