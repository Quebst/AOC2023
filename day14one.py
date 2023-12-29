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




def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    grid = [list(line) for line in lines]

    shift(grid)
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