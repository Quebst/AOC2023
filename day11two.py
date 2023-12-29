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

blank_rows = []
blank_columns = []


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    grid = [list(line) for line in lines]
    galaxies = {}

    egrid = expansion(grid)

    counter = 1
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == "#":
                galaxies[counter] = [i, j]
                counter += 1

    distances = 0

    i = counter - 1
    while i > 0:
        gal = galaxies.popitem()
        galx, galy = gal[1]
        j = i - 1
        while j > 0:
            jx, jy = galaxies[j]
            # for x add to a million each time a blank_row is found
            xdist = abs(galx - jx)
            for row in blank_rows:
                if (galx < row < jx) or (jx < row < galx):
                    xdist += 999999
            # for y add to a million each time a blank_colum is found
            ydist = abs(galy - jy)
            for column in blank_columns:
                if (galy < column < jy) or (jy < column < galy):
                    xdist += 999999
            distances += xdist + ydist
            j -= 1

        i -= 1

    print("Total Distance is: ", distances)
    print(blank_rows)
    print(blank_columns)


def expansion(grid):
    open_columns = []

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
            blank_columns.append(width)

        width -= 1

    width = len(grid[0])

    k = length - 1
    while k >= 0:
        if "#" not in grid[k]:
            print(f"Row {k} is empty")
            blank_rows.append(k)

        k -= 1

    return grid


if __name__ == "__main__":
    main()
