from copy import copy, deepcopy


class State():

    def __init__(self, program, choice=None, stack=[]):
        """Init function.

        Arguments:
            program {[list]} -- the list of instruction we want to compute space state

        Keyword Arguments:
            choice {[int]} -- number to choose which instruction to execute (default: {None})
            stack {list} -- the stack of instruction (default: {[]})
        """
        self.program = program
        self.choice = choice
        self.stack = stack

    def evaluation(self):
        """Evaluate the current state and return the result(s)

        Returns:
            [list] -- list of new state
        """
        # if the list is empty, it's the end
        if not(self.program):
            return [self]
        # if await instruction we loop over every possible choice and the await loop isn't empty
        if "await" in str(self.program[0]) and self.program[0]['await']:
            res = []
            for choice in range(len(self.program[0]['await'])):
                # we copy the dictionnary to change it
                dict_to_await = copy(self.program[0])
                # get the value/function to put on stack
                value_to_stack = dict_to_await['await'][choice]
                # remove this value from the list in dictionnary
                dict_to_await['await'] = dict_to_await['await'][0: choice] + dict_to_await['await'][choice + 1:]
                # add the new dictionnary to program
                program = [dict_to_await] + copy(self.program[1:])
                # add the createad state to the result
                res.append(State(program, choice, copy(self.stack) + [value_to_stack]))
            return res
        # if the await loop is empty
        elif "await" in str(self.program[0]):
            return [State(self.program[1:], None, copy(self.stack))]
        else:
            return [State(self.program[1:], None, copy(self.stack) + [self.program[0]])]

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, str(self.__dict__))

    def __eq__(self, other):
        return (self.program == other.program) and (self.stack == other.stack)

    def __hash__(self):
        s = str(self.program) + str(self.stack)
        return hash(s)


class FixPoint():

    def __init__(self, initial_state):
        self.space_states = set([])
        self.initial_state = initial_state

    def run(self):
        # first run
        for ele in self.initial_state.evaluation():
            self.space_states.add(ele)
        end = False
        # fix point
        while not(end):
            # we copy the current space state
            copy_space_states = deepcopy(self.space_states)
            # for every state in the space state
            for state in copy_space_states:
                # we compute the eval -> the new states
                for new_state in state.evaluation():
                    # add it to the space state
                    self.space_states.add(new_state)
            # if the copy is equal to the new, it means we reach a fix poit, so stop the loop
            if self.space_states == copy_space_states:
                end = True

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self.space_states)

    def print_space_state(self):
        for ele in self.space_states:
            print(ele, '\n')


if __name__ == '__main__':
    s = State([{'await': [4, 5, 6]}, 7])
    fix_point = FixPoint(s)
    fix_point.run()
    fix_point.print_space_state()
