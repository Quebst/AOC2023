#from functools import lru_cache
from copy import deepcopy

raw_data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# lower than 151482
# lower than 107212
# lower than 107230


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    grid = [list(line) for line in lines]
    cycles = 4000000000
    check_cycle = ""
    
    i = 0
    while i < (10048):
        if i % 4 == 0 and check_cycle == grid:
            print("Cycle repeats at: ", i)
        if i == 10000:
            print("10000 Cycles")
            check_cycle = deepcopy(grid)
        
        shift(grid)
        grid = rotate_clock(grid)
        # for row in grid:
        #     print(row)
        # print("--------------------------------------")
        i += 1
    
    #grid = rotate_counter(grid)
    
    
    # for row in grid:
    #     print(row)
    print(find_score(grid))
      
def find_score(grid):
    points = len(grid)
    total_score = 0    
    
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "O":
                total_score += points
        points -= 1
        
    return total_score
    
def rotate_counter(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

def rotate_clock(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def shift(grid):
    # a list to hold all rocks blocking the roll north
    blocks = [-1 for x in range(len(grid[0]))]
    
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "#":
                blocks[j] = i
            elif char == "O":
                grid[i][j] = "."
                blocks[j] += 1
                grid[blocks[j]][j] = "O"
      
    
if __name__ == "__main__":
    main()  