
raw_data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = []
    height = len(lines) + 2
    width = len(lines[0]) + 2
    start = []
    locs = set()
    
    steps = 0
    
    board = [["#" for _ in range(width)] for _ in range(height)]
    i, j = 1, 1
    while i < height - 1:
        j = 1
        while j < width - 1:
            board[i][j] = lines[i-1][j-1]
            if board[i][j] == "S":
                start = tuple([i, j])
                board[i][j] = "."
            j += 1
        i += 1
    
    print(f"Start is: {start}")
    #for line in board:
     #   print(line)
    
    locs.add(start)
    while steps < 64:
        new_locs = set()
        for loc in locs:
            i, j = loc
            checks = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            for c in checks:
                i, j = c
                if board[i][j] == ".":
                    new_locs.add(tuple([i, j]))
        locs = new_locs
        steps += 1
        
    print(f"There are {len(locs)} plots")
    
            
            


if __name__ == "__main__":
    main()
    
    