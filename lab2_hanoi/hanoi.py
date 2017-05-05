import sys

class Hanoi:
    def __init__(self, size):
        self.pegA = range(size, 0, -1)
        self.pegB = []
        self.pegC = []
        self.size = size
        self.moves = 0

    def display(self):
        """ Displays contents in each peg list """
        print("0: " + ' '.join(str(p) for p in self.pegA))
        print("1: " + ' '.join(str(p) for p in self.pegB))
        print("2: " + ' '.join(str(p) for p in self.pegC))
        print

    def solve(self):
        """ Start of solve routine, checks initial conditions """
        if self.size == 1:
            self.move(self.pegA, self.pegB)
        elif self.size > 1:
            """ choose if ring 1 moves to B or C """
            """ if size is even move A to B, odd move A to C """
            if self.is_odd(self.size):
                self.han_recursion(self.pegA, self.pegB, self.pegC)
            else:
                self.han_recursion(self.pegA, self.pegC, self.pegB)
        else:
            raise Exception("Size must be 1 or greater.")

    def move(self, from_peg, to_peg):
        """ Moves disk from_peg to to_peg """
        self.moves += 1
        print("Move Number: {}".format(self.moves))
        to_peg.append(from_peg.pop())
        self.display()

    def han_recursion(self, start, first, end):
        """ Recursive method of hanoi.py. """
        """ Moves 1-3 always move disks 1&2 to from start peg to end peg """
        self.move(start, first)
        self.move(start, end)
        self.move(first, end)
        """ Move 4: moves smallest ring in start or first peg to the other peg
        Need to check if either start or first are empty
        If both both are empty then recursion is complete """
        if not start:
            if not first:
                print "Completed"
            else:
                # print "start empty, first not - move first to start"
                self.move(first, start)
                if self.is_odd(start[-1]):
                    self.han_recursion(end, first, start)
                else:
                    self.han_recursion(end, start, first)
        else:
            if not first:
                # print "first empty, start not - move start to first"
                self.move(start, first)
                if self.is_odd(first[-1]):
                    self.han_recursion(end, start, first)
                else:
                    self.han_recursion(end, first, start)
            else:
                # print "both not empty - check which is smaller"
                if start[-1] < first[-1]:
                    self.move(start, first)
                    if self.is_odd(first[-1]):
                        self.han_recursion(end, start, first)
                    else:
                        self.han_recursion(end, first, start)
                else:
                    self.move(first, start)
                    if self.is_odd(start[-1]):
                        self.han_recursion(end, first, start)
                    else:
                        self.han_recursion(end, start, first)

    def is_odd(self, value):
        return value % 2

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
