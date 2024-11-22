
def solve(puzzle):
    start_floor = 0
    end_floor = inefficient_recursive(puzzle, start_floor)
    return end_floor

def inefficient_recursive(puzzle, floor):
    if puzzle == '':
        return floor
    else:
        if puzzle[0] == '(':
            floor += 1
        if puzzle[0] == ')':
            floor -= 1
        the_rest_of_puzzle = puzzle[1:]
        return inefficient_recursive(the_rest_of_puzzle, floor)

def main():
    with open('input.txt') as file:
        puzzle = file.read()
        print(solve(puzzle))

if __name__ == '__main__':
    main()
