# Helper classes


# handles ranges of numbers
class Ranger:
    def __init__(self, ran):
        self.ran = ran

    # takes a Ranger and a range to further restrict size
    # results will be equal or smaller, never bigger
    def exor(self, mag, direct):
        new_ran = []
        low, high = self.ran
        if low < mag < high:
            if direct == "<":
                new_ran = [low, mag]
            elif direct == ">":
                new_ran = [mag, high]
        else:
            new_ran = [low, high]

        return new_ran

    # take in a ranger, mag, direction, return two new rangers
    # second ranger is None if mag not in current range
    # first ranger is affirmative anser
    def split_range(self, mag, direct):
        low, high = self.ran
        mag = int(mag)
        new_ran = []
        second_ran = None
        if low < mag < high:
            if direct == "<":
                new_ran = [low, mag - 1]
                second_ran = [mag, high]
            elif direct == ">":
                new_ran = [mag + 1, high]
                second_ran = [low, mag]
        else:
            new_ran = [low, high]

        new_ran = Ranger(new_ran)
        second_ran = Ranger(second_ran)
        return new_ran, second_ran

    def magnitude(self):
        low, high = self.ran
        return 1 + high - low

    def __repr__(self):
        return f"Ranges are: {self.ran} "


# Node class with left and right children, rans = ranges, stat = accepted, regjected, or active
class Node:
    def __init__(self, rans, stat, left, right):
        self.rans = rans
        self.left = left
        self.right = right
        self.stat = stat
        self.x = rans[0]
        self.m = rans[1]
        self.a = rans[2]
        self.s = rans[3]

    def total(self):
        xx = self.x.magnitude()
        mm = self.m.magnitude()
        aa = self.a.magnitude()
        ss = self.s.magnitude()

        return xx * mm * aa * ss

    def __repr__(self):
        return (
            f"Node status: {self.stat} x: {self.x} m: {self.m} a: {self.a} s: {self.s}"
        )
