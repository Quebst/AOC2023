raw_data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

raw_data2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    blocks = [block.strip() for block in read_data.split("\n\n")]
    score = 0
    for block in blocks:
        lines = block.splitlines()
        grid = [list(line) for line in lines]

        # score += find_hor(grid) * 100
        # vert_grid = [" ".join(map(str, row)) for row in zip(*grid)]
        vert_grid = list(map(list, zip(*grid)))

        score += scan_grid(grid, vert_grid)
        print(score)

    print("Score is: ", score)


def scan_grid(grid, vert_grid):
    original_hor = find_hor(grid, -1)
    original_vert = find_hor(vert_grid, -1)

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            # switch each char on grid and vert
            # check for reflections, return values
            new_hor = 0
            new_vert = 0
            alt = ""
            orig = grid[i][j]
            if orig == ".":
                alt = "#"
            elif orig == "#":
                alt = "."
            grid[i][j] = alt
            vert_grid[j][i] = alt

            new_hor = find_hor(grid, original_hor)
            new_vert = find_hor(vert_grid, original_vert)

            if new_hor > 0:
                return new_hor * 100
            if new_vert > 0:
                return new_vert

            grid[i][j] = orig
            vert_grid[j][i] = orig


# find horizontal mirrors, return bottom of two rows
def find_hor(hlines, exclude):
    possibles = []
    old_line = ""
    confirmed = 0

    for i, hline in enumerate(hlines):
        if hline == old_line:
            possibles.append(i)
        old_line = hline

    if exclude in possibles:
        possibles.remove(exclude)

    for poss in possibles:
        up = poss - 1
        down = poss

        while up >= 0 and down < len(hlines):
            if hlines[up] != hlines[down]:
                break
            up -= 1
            down += 1
        else:
            confirmed = poss

    return confirmed


if __name__ == "__main__":
    main()
