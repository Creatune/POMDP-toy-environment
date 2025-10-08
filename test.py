import random

class Environment:
    def __init__(self):
        self.states = [('A', 1, 1), ('B', 1, 1), ('A', -1, 1), ('B', -1, 1), ('A', -1, -1), ('B', -1, -1), ('A', 1, -1), ('B', 1, -1)]
        self.actions = ['Move', 'Toggle', 'Stay']
        self.p = 0.7
        self.q = 0.7
    
    def O(self, s):
       #  only able to get the light status of the current room correctly with probability 0.9
        if s[0] == 'A':
            return [(s[1], 0.9), (-s[1], 0.1)]
        else:
            return [(s[2], 0.9), (-s[2], 0.1)]

    def T(self, s, a):
        if a == 'Move':
            if s[0] == 'A':
                return [('B', s[1], s[2], self.p), (s[0], s[1], s[2], 1-self.p)]
            else:
                return [('A', s[1], s[2], self.p), (s[0], s[1], s[2], 1-self.p)]
        elif a == 'Toggle':
            if s[0] == 'A':
                return [(s[0], -s[1], s[2], self.q), (s[0], s[1], s[2], 1-self.q)]
            else:
                return [(s[0], s[1], -s[2], self.q), (s[0], s[1], s[2], 1-self.q)]
        else:
            return [(s[0], s[1], s[2], 1)]


    def R(self, s):
        if s[0] == 'B' and s[2] == 1:
            return 1
        else:
            return 0
