"""
Solve the Advent of Code 2015 Day 1 Part 1 puzzle.

How to run:

$ python solvepuzzle.py filename.txt

or

$ python solvepuzzle.py

if your puzzle is in input.txt

"""

def solve(puzzle):
    """Return the integer that is the answer to the puzzle."""
    # uncomment/comment to pick an implementation
    return count(puzzle)
    # return sum_generator(puzzle)
    # return counter(puzzle)
    # return imperative(puzzle)
    # return sum_map(puzzle)
    # return replace_eval(puzzle)

def count(puzzle):
    """Use str.count() to find the answer."""
    up = puzzle.count('(')
    down = puzzle.count(')')
    floor = up - down
    return floor

def sum_generator(puzzle):
    """Use sum() and a generator expression to find the answer."""
    instructions = {'(': 1, ')':-1}
    numbers = (instructions[c] for c in puzzle)
    floor = sum(numbers)
    return floor

import collections
def counter(puzzle):
    """Use collections.Counter to find the answer."""
    c = collections.Counter(puzzle)
    floor = c['('] - c[')']
    return floor

def imperative(puzzle):
    """Use for loop to find the answer."""
    floor = 0
    for character in puzzle:
        if character == '(':
            floor += 1
        if character == ')':
            floor -= 1
    return floor

def sum_map(puzzle):
    """Use sum() and map() to find the answer."""
    instructions = {'(': 1, ')':-1}
    function = lambda c: instructions[c]
    numbers = map(function, puzzle)
    floor = sum(numbers)
    return floor

def replace_eval(puzzle):
    """Transform the puzzle into a Python expression and use eval() on to find the answer."""
    half_translated = puzzle.replace('(','+1')
    formula = half_translated.replace(')','-1')
    floor = eval(formula)
    return floor

def compare_performance(puzzle):
    """
    Compare the performance of different implementations

    >>> import solvepuzzle
    >>> a = open('input.txt').read()
    >>> solvepuzzle.compare_performance(a)
    Running count...OK
    Running sum_generator...OK
    Running counter...OK
    Running imperative...OK
    Running sum_map...OK
    Running replace_eval...OK
    0.079718ms      count
    1.085038ms      sum_generator
    1.152964ms      counter
    1.413505ms      imperative
    2.166971ms      sum_map
    22.533185ms     replace_eval
    """
    import timeit
    functions = [count, sum_generator, counter, imperative, sum_map, replace_eval]
    results = []
    for f in functions:
        print(f'Running {f.__name__}...', end='', flush=True)
        timer = timeit.Timer('solve(puzzle)', globals={'solve': f, 'puzzle': puzzle})
        number, _ = timer.autorange()
        time = min(timer.repeat(number=number))/number*1000
        results.append( (time, f.__name__) )
        print('OK')
    results.sort()
    for time, name in results:
        print(f'{time:f}ms\t{name}')

def main():
    """Read the puzzle from a file, call solve() and print its return value. File name is input.txt by default or the first argument to the program."""
    filename = 'input.txt'
    import sys
    if len(sys.argv)>1:
        filename = sys.argv[1]
    with open(filename) as file:
        puzzle = file.read()
        print(solve(puzzle))

if __name__ == '__main__':
    main()
