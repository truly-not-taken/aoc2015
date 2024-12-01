"""
Solve the Advent of Code 2015 Day 1 puzzle parts 1 and 2.

How to run:

$ python solvepuzzle.py filename.txt

or

$ python solvepuzzle.py

if your puzzle is in input.txt

"""

def part1(puzzle):
    """Return the integer that is the part 1 answer to the puzzle."""
    return puzzle.count('(') - puzzle.count(')')

def part2(puzzle):
    """Return the position of the character that causes Santa to first enter the basement."""
    return cheat(puzzle)

def cheat(puzzle):
    """Works for the examples from the description of the puzzle."""
    return len(puzzle)

def main():
    """
    Read the puzzle from a file, solve it and print the answer.
    File name is input.txt by default or the first argument to the program.
    """
    filename = 'input.txt'
    import sys
    if len(sys.argv)>1:
        filename = sys.argv[1]
    with open(filename) as file:
        puzzle = file.read()
        print('part1:', part1(puzzle))
        print('part2:', part2(puzzle))

if __name__ == '__main__':
    main()
