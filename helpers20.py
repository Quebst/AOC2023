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


