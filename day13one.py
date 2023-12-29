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

        score += find_hor(lines) * 100
        vert_grid = [" ".join(map(str, row)) for row in zip(*grid)]
        score += find_hor(vert_grid)
        print(score)

    print("Score is: ", score)


# find horizontal mirrors, return bottom of two rows
def find_hor(hlines):
    possibles = []
    old_line = ""
    confirmed = 0

    for i, hline in enumerate(hlines):
        if hline == old_line:
            possibles.append(i)
        old_line = hline

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
