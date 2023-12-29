raw_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    grid = [list(line) for line in lines]
    galaxies = {}

    for row in grid:
        print(row)
    egrid = expansion(grid)
    
    print("------------------------------------------")
    for row in egrid:
        print(row)
     
    counter = 1    
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == "#":
                galaxies[counter] = [i, j]
                counter += 1
                
    print(galaxies)
    print(counter)
    
    distances = 0
    

    
    i = counter - 1
    while i > 0:
        print(galaxies[i])
        gal = galaxies.popitem()
        print(gal[1])
        galx, galy = gal[1]
        j = i - 1
        while j > 0:
            jx, jy = galaxies[j]
            xdist = abs(galx - jx)
            ydist = abs(galy - jy)
            distances += xdist + ydist
            j -= 1
        
        i -= 1
        
    print("Total Distance is: ", distances)
        
        
        
        
        
#def gal_counter(gal):
    
        

def expansion(grid):
    open_columns = []
    open_rows = []
    
    width = len(grid[0]) - 1
    length = len(grid)
    
    print(width)
    while width >= 0:
        i = 0
        open_columns = []
        while i < length:
            open_columns.append(grid[i][width])
            i += 1
            
    
        if "#" not in open_columns:
            j = 0
            for j in range(len(grid)):
                grid[j].insert(width + 1, ".")
        
        width -= 1
        
    width = len(grid[0])
    dots = ["." for _ in range(width)]
    
    k = length - 1
    while k >= 0:
        if "#" not in grid[k]:
            print(f"Row {k} is empty")
            grid.insert(k, dots)
            
        k -= 1
                
    return grid
        
        
        
if __name__ == "__main__":
    main()
