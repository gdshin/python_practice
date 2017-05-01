import sys

class Hanoi:
    def __init__(self, size):
        self.pegA = range(size, 0, -1)
        self.pegB = []
        self.pegC = []
        self.moves = 0

    def display(self):
        """ Displays contents in each peg list """
        print("0: " + ' '.join(str(p) for p in self.pegA))
        print("1: " + ' '.join(str(p) for p in self.pegB))
        print("2: " + ' '.join(str(p) for p in self.pegC))
        print

    def solve(self):
        self.han_recursion(len(self.pegA), self.pegA, self.pegC, self.pegB)

    def move(self, from_peg, to_peg):
        """ Moves disk from_peg to to_peg """
        self.moves += 1
        print("Move Number: {}".format(self.moves))
        to_peg.append(from_peg.pop())
        self.display()

    def han_recursion(self, n, start, helper, end):
        if n == 1:
            self.move(start, end)
        else:
            self.han_recursion(n - 1, start, end, helper)
            self.han_recursion(1, start, helper, end)
            self.han_recursion(n - 1, helper, start, end)

if len(sys.argv) != 2:
    raise Exception("Must have 1 argument.")
try:
    value = int(sys.argv[1])
except ValueError:
    print("Argument must be an integer.")
    pass

h = Hanoi(value)
h.display()
h.solve()
