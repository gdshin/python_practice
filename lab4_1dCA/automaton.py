
"""
A 1dCA is composed of the following elements:
1. An array of cells, each of which has a state (represented by a number between
        0 and the maximum number of states minus 1).
2. A neighborhood radius, which states how many cells in either direction affect
        the next state of any given cell. The cell's next state depends only on
        the states of these cells as well as its own current state.
3. A state transition table that determines which state to set a given cell to,
        given the previous state of the cell and the states of the cells in its
        neighborhood.

We will add one extra rule to simplify our program: the next state of a given
cell depends only on the sum of the states of the cells in its neighborhood
and its own state.

You are to write a python module called automaton.py which implements a 1dCA
with the following characteristics:
        1. The above updating rules are implemented.
        2. An arbitrary sized cell array can be specified.
        3. An arbitrary number of states can be specified.
        4. An arbitrary number of nearest neighbors can be specified.
        5. An arbitrary update rule (state transition table) can be specified.
Note that the size of the state transition table is a function of the number of
states and the number of neighbors.
"""


class cellular_automaton_1d:
    __init__(self, size, states, neighbors, trans_tbl):
        """ default for states, nearest neighbors, state transition table """
        self.size = size
        self.states = states
        self.neighbors = neighbors
        self.trans_tbl = trans_tbl

    generate_random_table(self):
        """ empty """

    random_initialize(self):
        """ empty """

    update(self):
        """ empty """

    get_states(self):
        """ empty """

    dump(self):
        """ empty """

if __name__ == "__main__":
    try:
        # Arguments here to the constructor are:
        # size of cell array, number of states, number of neighbors (on each
        # side), the state transition table.
        a = cellular_automaton_1d(70, 2, 1, [0, 1, 1, 0])
        a.random_initialize()
        a.dump()

        for i in range(100):
            a.update()
            a.dump()
    except ...  # whatever can be thrown in the try block
