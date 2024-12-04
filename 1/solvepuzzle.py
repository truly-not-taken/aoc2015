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
    # return cheat(puzzle)
    # return reuse_part1(puzzle)
    # return imperative(puzzle)
    # return for_enum(puzzle)
    # return for_dict(puzzle)
    # return generator(puzzle)
    # return compr_index(puzzle)
    # return compr_len(puzzle)
    return better_imperative(puzzle)

def cheat(puzzle):
    """Works for examples from the description of the puzzle."""
    return len(puzzle)

def reuse_part1(puzzle):
    """Use part1() in accordance with DRY principle."""
    for i in range(len(puzzle)+1):
        if part1(puzzle[:i]) == -1:
            return i

def imperative(puzzle):
    """Solve part 2 the boring way."""
    floor = 0
    position = 0
    for character in puzzle:
        position += 1
        if character == '(':
            floor += 1
        if character == ')':
            floor -= 1
        if floor == -1:
            return position

def for_enum(puzzle):
    """Solve part 2 using enumerate()."""
    floor = 0
    for i, character in enumerate(puzzle, start=1):
        if character == '(':
            floor += 1
        if character == ')':
            floor -= 1
        if floor == -1:
            return i

def for_dict(puzzle):
    """Solve part 2 using dict instead of ifs."""
    floor = 0
    for position, character in enumerate(puzzle, start=1):
        floor += {'(': 1, ')':-1}[character]
        if floor == -1:
            return position

def generator(puzzle):
    """Solve part 2 using generator function."""
    def gen_floor(x):
        """Generate floors Santa visits."""
        floor = 0
        for character in x:
            if character == '(':
                floor += 1
            if character == ')':
                floor -= 1
            yield floor

    position = 1
    floor = gen_floor(puzzle)
    while next(floor) >=0:
        position += 1
    return position

def compr_index(puzzle):
    """Solve part 2 using list comprehension and list.index()."""
    floor = 0
    return [floor:=floor+(1 if c=='(' else -1) for c in puzzle].index(-1)+1

def compr_len(puzzle):
    """Solve part 2 using list comprehension and len()."""
    floor = 0
    return len([floor:=floor+(1 if c=='(' else -1) for c in puzzle if floor>=0])

def better_imperative(puzzle):
    """Solve part 2 slightly less boring way."""
    floor = 0
    position = 0
    for character in puzzle:
        position, floor = position + 1 , floor + (1 if character == '(' else -1)
        if floor == -1:
            return position

def benchmark(puzzle):
    """
    Compare the performance of different implementations

    >>> import solvepuzzle
    >>> solvepuzzle.benchmark('('*500+')'*10000)
    Running cheat........................OK
    Running reuse_part1...........OK
    Running imperative...............OK
    Running for_enum...............OK
    Running for_dict..............OK
    Running generator..............OK
    Running compr_index.............OK
    Running compr_len..............OK
    Running better_imperative...............OK
    0.000303ms      cheat
    0.233554ms      better_imperative
    0.282934ms      imperative
    0.318613ms      for_enum
    0.516514ms      generator
    0.636725ms      compr_len
    0.653871ms      for_dict
    1.734715ms      compr_index
    4.552847ms      reuse_part1
    >>> solvepuzzle.benchmark('('*9999+')'*10000)
    Running cheat........................OK
    Running reuse_part1......OK
    Running imperative...........OK
    Running for_enum...........OK
    Running for_dict..........OK
    Running generator..........OK
    Running compr_index...........OK
    Running compr_len...........OK
    Running better_imperative...........OK
    0.000310ms      cheat
    4.158089ms      compr_len
    4.360929ms      compr_index
    5.453742ms      better_imperative
    6.848317ms      imperative
    7.095255ms      for_enum
    11.477133ms     generator
    14.526480ms     for_dict
    1165.639348ms   reuse_part1
    """
    def dot(*args):
        """Print a dot. That is it."""
        print('.',end='',flush=True)
        return 0
    import timeit
    functions = [cheat, reuse_part1, imperative, for_enum, for_dict, generator, compr_index, compr_len, better_imperative]
    results = []
    for f in functions:
        print(f'Running {f.__name__}', end='', flush=True)
        timer = timeit.Timer('solve(puzzle)', globals={'solve': f, 'puzzle': puzzle})
        number, _ = timer.autorange(dot)
        time = min(timer.timeit(number) + dot() for i in range(5)) / number * 1000
        results.append( (time, f.__name__) )
        print('OK')
    results.sort()
    for time, name in results:
        print(f'{time:f}ms\t{name}')

def benchmark2():
    """Print a table of numbers for a spreadsheet to draw a fun chart."""
    import timeit
    functions = [cheat, reuse_part1, imperative, for_enum, for_dict, generator, compr_index, compr_len, better_imperative]
    results = [['Size_of_input']+list(range(1000, 30001, 1000))]
    for f in functions:
        print(f'Running {f.__name__}', end='', flush=True)
        results.append([f.__name__])
        for size in results[0][1:]:
            puzzle = '('*(size//7) + ')'*(size-size//7)
            timer = timeit.Timer('solve(puzzle)', globals={'solve': f, 'puzzle': puzzle})
            number, time = timer.autorange()
            print('.',end='',flush=True)
            time = time / number * 1000
            results[-1].append(time)
        print('OK')
    for line in zip(*results):
        print(*line)


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
