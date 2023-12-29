from itertools import cycle
from math import lcm

raw_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

raw_data2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    directions = cycle(lines.pop(0))
    del lines[0]
    nodes = {}
    steps = 0
    currents = []
    total_steps = []

    for line in lines:
        source = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[source] = [left, right]
        if source[2:] == "A":
            currents.append(source)
    print(currents)
    j = 0
    while j < len(currents):
    
        steps = 0
        
        for i in directions:
            lookup = currents[j]
            if i == "L":
                currents[j] = nodes[lookup][0]
            else:
                currents[j] = nodes[lookup][1]
            steps += 1

            if currents[j][2:] == "Z":
                total_steps.append(steps)
                break
        j += 1
        
    print(total_steps)    
        
    print(lcm(*total_steps))

if __name__ == "__main__":
    main()
