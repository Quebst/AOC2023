
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
    #lines = read_data.splitlines()
    workflows, parts = raw_data.split("\n\n")
    
    lines = workflows.splitlines()
    works = {}
    part_list = []
    
    for line in lines:
        key, orders = line.split("{")
        orderlist = []
        orders = orders[:-1].split(",")
        
        for order in orders:
            orderlist.append(order)
        
        works[key] = orderlist
        
    print(works)
    
    lines = parts.splitlines()
    
    for i, line in enumerate(lines):
        atts = line[1:-1].split(",")
        part_list.append(Part(i, int(atts[0][2:]), int(atts[1][2:]), int(atts[2][2:]), int(atts[3][2:])))
        
    for part in part_list:
        print(part)
        sort_part(works, part.x, part.m, part.a, part.s)
        
        
    print(accepted)
    print("Sum is: ", sum(accepted))

# use eval() to check truth of proposition
def sort_part(works, x, m, a, s):
    key = "in"
    goal = 'none'
    
    while True:
        wfs = works[key]
        i = 0
        for wf in wfs:
            if goal == "A":
                accepted.append(x + m + a + s)
                return
            if goal == "R":
                return
            
            if ":" in wf:
                prop, result = wf.split(":")
                #print("----------------")
                if eval(prop):
                    if result == "R":
                        return
                    elif result == "A":
                        goal = "A"
                    else:
                        key = result
                        break
                else:
                    continue
                    
                
            else:
                if wf == "R":
                    return
                elif wf == "A":
                    goal = "A"
                else:
                    key = wf
        

class Part:
    def __init__(self, ind, x, m, a, s):
        self.ind = ind
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        
    def __str__(self):
        return f"Part num:{self.ind} x:{self.x} m:{self.m} a:{self.a} s:{self.s} "

if __name__ == "__main__":
    main()
