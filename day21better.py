from copy import copy

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
    lines = raw_data.splitlines()
    board = []
    height = len(lines)
    width = len(lines[0])
    board = []
    start = []
    locs = set()
    visited = set()
    dotcount = 0
    steps = 0
    
    # o for odd, 1 for even
    vcount = 1
    old_locs = set()
    
    i= 0
    while i < height:
        j = 0
        row = []
        while j < width:
            row.append(lines[i][j])
            if lines[i][j] == ".":
                dotcount += 1
            elif lines[i][j] == "S":
                start = tuple([i, j, 0, 0])
                row[j] = "."
            j += 1
        board.append(row)
        i += 1
    
    print(f"Start is: {start} height: {height} width: {width}")
    # for line in board:
    #     print(line)
    
    locs.add(start)
    # hd is horizonal panel, vd vertical panel location
    while steps < 5000:
        # if (steps - 150) % 262 == 0:
        #     mag = (steps - 150) // 262
        #     vcount = trim(visited, mag, vcount)
        
        new_locs = set()
        for loc in locs:
            i, j, id, jd = loc
            checks = ([i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1])
            for c in checks:
                newjd = jd
                newid = id
                i, j = c
                # adjust for infinite fields
                if i < 0:
                    i = height - 1
                    newid -= 1
                elif i >= height:
                    i = 0
                    newid += 1
                elif j < 0:
                    j = width - 1
                    newjd -= 1
                elif j >= width:
                    j = 0
                    newjd += 1
                    
                if board[i][j] == ".":
                    if tuple([i, j, newid, newjd]) not in old_locs:
                        new_locs.add(tuple([i, j, newid, newjd]))
                        # if steps % 2 == 0:
                        #     visited.add(tuple([i, j, newid, newjd]))
        
        # set to 1 for even (add 1 to count), 0 for odd
        if steps % 2 == 1:
        #     visited.update(*locs)
            vcount += len(new_locs)
        old_locs = locs
        locs = new_locs
        steps += 1
         
    print(f"There are visited: {len(visited)}, vcount: {vcount}, total {len(visited) + vcount}  dotcount: {dotcount}")
    
# 7717 for 0,0 (evens)  7693 for 1,0 (odds)
def trim(visit, mag, vcount):
    xhi = mag
    xlow = 0 - mag
    EVEN = 7717
    ODD = 7693
    
    vcount += EVEN * 4 + ODD * 4
    
    for i in range(xlow, xhi):
        for v in visit.copy():
                if v[2] == i or v[3] == i:
                    visit.discard(v)
    
    return vcount
    

def counted(visit):
    panel = 0
    count = 0 
    
    for v in visit:
        a, b, c, d = v
        if c == -1 and d == 0:
            count += 1
    
    print(f"Panel {panel} has count: {count}")
    
     
            
if __name__ == "__main__":
    main()
    
    