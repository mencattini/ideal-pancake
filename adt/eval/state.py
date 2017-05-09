from stew.core import Sort, generator, operation
from stew.matching import var
from collections.abc import Sequence
from adt.types.expr_list import Expr_list
from adt.types.nat import Nat
from adt.types.expr import Expr


class State(Sort):

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], Sequence):
            list_args = args[0]

            Sort.__init__(self)
            if len(list_args) == 0:
                self._generator = State.cons
                self._generator_args = {
                    "program": Expr_list.empty(),
                    "choice": Nat.zero(),
                    "stack": Expr_list.empty()}
            else:
                self._generator = State.cons
                self._generator_args = {
                    "program": list_args[0],
                    "choice": list_args[1],
                    "stack": list_args[2]}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> State:
        return State.cons(
            program=Expr_list.empty(),
            choice=Nat.zero(),
            stack=Expr_list.empty())

    @generator
    def cons(program: Expr_list, choice: Nat, stack: Expr_list) -> State:
        pass

    @operation
    def add_instr_stack(state: State, expr: Expr) -> State:
        if state == State.cons(program=var.x, choice=var.y, stack=var.z):
            new_stack = Expr_list.cons(tail=var.z, head=expr)
            return State.cons(program=var.x, choice=var.y, stack=new_stack)
        else:
            raise ValueError("The types of the args are wrong")

    @operation
    def change_choice(state: State, new_choice: Nat) -> State:
        if state == State.cons(program=var.x, choice=var.y, stack=var.z):
            return State.cons(program=var.x, choice=new_choice, stack=var.z)
        else:
            raise ValueError("The types of the args are wrong")

    @operation
    def add_instr_program(state: State, expr: Expr) -> State:
        if state == State.cons(program=var.x, choice=var.y, stack=var.z):
            new_program = Expr_list.cons(tail=var.x, head=expr)
            return State.cons(program=new_program, choice=var.y, stack=var.z)
        else:
            raise ValueError("The types of the args are wrong")
