from helpers19 import Node, Ranger
from copy import deepcopy


raw_data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

accepted = []
rejected = []


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    workflows, parts = read_data.split("\n\n")
    total_ways = 0
    lines = workflows.splitlines()
    works = {}

    for line in lines:
        key, orders = line.split("{")
        orders = orders[:-1].split(",")
        works[key] = orders

    first_node = Node(
        [Ranger([1, 4000]), Ranger([1, 4000]), Ranger([1, 4000]), Ranger([1, 4000])],
        "none",
        None,
        None,
    )
    treeit(works, first_node, "in")

    for a in accepted:
        total_ways += a.total()

    print(f"Total ways: {total_ways}")
    print("Out of    : 256000000000000")


# key = "in" to start
def treeit(works, nodel, key):
    goal = nodel.stat
    if goal == "A":
        accepted.append(nodel)
        return True
    elif goal == "R":
        rejected.append(nodel)
        return False

    while True:
        wfs = works[key]
        for wf in wfs:
            if goal == "A":
                accepted.append(nodel)
                return True
            elif goal == "R":
                rejected.append(nodel)
                return False
            elif goal == None:
                return False

            if ":" in wf:
                prop, result = wf.split(":")
                direction = prop[1:2]
                attr = prop[:1]
                mag = prop[2:]
                one_node = deepcopy(nodel)

                if attr == "x":
                    rone, rtwo = nodel.x.split_range(mag, direction)
                    one_node.x = rone
                    nodel.x = rtwo
                elif attr == "m":
                    rone, rtwo = nodel.m.split_range(mag, direction)
                    one_node.m = rone
                    nodel.m = rtwo
                elif attr == "a":
                    rone, rtwo = nodel.a.split_range(mag, direction)
                    one_node.a = rone
                    nodel.a = rtwo
                elif attr == "s":
                    rone, rtwo = nodel.s.split_range(mag, direction)
                    one_node.s = rone
                    nodel.s = rtwo
                one_node.stat = result
                treeit(works, one_node, result)

            else:
                if wf == "R":
                    rejected.append(nodel)
                    return False
                elif wf == "A":
                    accepted.append(nodel)
                    return True
                else:
                    key = wf


if __name__ == "__main__":
    main()
