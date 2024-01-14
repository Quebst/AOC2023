
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

raw_data2 = """...........
...........
...........
...........
...........
...........
...........
...........
...........
...........
..........."""




EVEN = 7717
ODD = 7693
PANELS = 202300
LPANELS = PANELS - 1 

N = 131
P = 65
# n-1 to reach edge
#center spot is 66
# top is 1, bottom is 131, left is 1, right is 131


# 4 courners
# evens
# odds
# whole panels
values = [5816, 5844, 5789, 5817,
6749*LPANELS, 6757*LPANELS, 6776*LPANELS, 6785*LPANELS,
980*PANELS, 970*PANELS, 981*PANELS, 980*PANELS,
(PANELS - 1)*(PANELS - 1)*EVEN, PANELS*PANELS*ODD
]

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = []
    height = len(lines) + 2
    width = len(lines[0]) + 2
    start = (131, 1)
    #start = (66,66)
    #start = (66, 67)
    locs = set()
    
    steps = 1
    
    board = [["#" for _ in range(width)] for _ in range(height)]
    i, j = 1, 1
    while i < height - 1:
        j = 1
        while j < width - 1:
            board[i][j] = lines[i-1][j-1]
            if board[i][j] == "S":
                #start = tuple([i, j])
                board[i][j] = "."
            j += 1
        i += 1
    
    print(f"Start is: {start}")
    #for line in board:
     #   print(line)
    
    locs.add(start)
    while steps < P:
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
    print(f"Total plots covered are {sum(values)}")
    #pboard(board, locs)
            
# board size 11 by 11, mag = 5, full takes 9 (5+4)
#  
 
# 131 square board, half is 65
# 
            
def pboard(board, locs):
    for loc in locs:
        x, y = loc
        board[x][y] = "0"
    for b in board:
        print(b)
        
    return True
    

if __name__ == "__main__":
    main()
    
    