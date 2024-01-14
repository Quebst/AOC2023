from collections import deque
from math import lcm

raw_data = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

raw_data2 = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


# pulses are a two part list, [0] is high/low (true, false) [1] is source
def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    mods = {}

    pulseq = deque()
    highcount = 0
    lowcount = 0
    b_targets = []

    # create mods dictionary, values are either Flip or Conju
    for line in lines:
        mod, targets = line.split("->")
        mod = mod.strip()
        targets = list(map(str.strip, targets.split(",")))

        if mod == "broadcaster":
            b_targets = targets
        else:
            mtype = mod[:1]
            if mtype == "%":
                mods[mod[1:]] = Flip(targets)
            elif mtype == "&":
                mods[mod[1:]] = Conju(targets)

    # initialize all conju.last to false
    for mod in mods:
        targets = mods[mod].targets
        for tar in targets:
            if tar not in mods:
                continue
            if isinstance(mods[tar], Conju):
                mods[tar].last[mod] = False

    # Push button
    i = 0
    # Find Cycle ['mp', 'qt', 'qb', 'ng'] All must be high
    cyclel = [3917, 4007, 4027, 3919]
    while i < 50000:
        i += 1
        lowcount += 1
        for tar in b_targets:
            pulseq.append([False, tar, "broadcast"])

        while pulseq:
            pul, dest, source = pulseq.popleft()
            if dest == "ng" and not pul:
                print(f"Cycles low at: {i}")
            # print(f"pul: {pul} dest: {dest} source: {source}")
            if dest == "rx" and not pul:
                print(f"Hit rx with {pul} at {i}")
                return

            if pul:
                highcount += 1
            else:
                lowcount += 1
            if dest not in mods:
                continue

            results = mods[dest].pulse([pul, source])
            if results:
                new_pul, new_dests = results
                for new_dest in new_dests:
                    pulseq.append([new_pul, new_dest, dest])

    print(f"Lowcount: {lowcount} Highcount: {highcount} Total: {lowcount * highcount}")
    print(lcm(*cyclel))


# low pulse is False, high is True
# %
class Flip:
    def __init__(self, targets):
        self.targets = targets
        self.power = False

    def __repr__(self):
        return f"Flip power: {self.power} targets: {self.targets}"

    # act if pul is false, else ignore
    def pulse(self, pul):
        state, source = pul
        if not state:
            self.power = not self.power
            if self.power:
                return True, self.targets
            else:
                return False, self.targets


# low pulse is False, high is True
# &
class Conju:
    def __init__(self, targets):
        self.targets = targets
        self.last = {}

    def __repr__(self):
        return f"Conju last: {self.last} targets: {self.targets}"

    def pulse(self, pul):
        state, source = pul
        self.last[source] = state
        if all(self.last.values()):
            return False, self.targets
        else:
            return True, self.targets


if __name__ == "__main__":
    main()
