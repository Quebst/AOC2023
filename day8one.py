from itertools import cycle

raw_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

raw_data2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = raw_data.splitlines()
    directions = cycle(lines.pop(0))
    del lines[0]
    nodes = {}
    steps = 0

    for line in lines:
        source = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[source] = [left, right]

    print(nodes)
    current = "AAA"

    for i in directions:
        if i == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        steps += 1

        if current == "ZZZ":
            break

    print(f"Found ZZZ in {steps} steps")


if __name__ == "__main__":
    main()
