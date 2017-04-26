from adt.types.relative_list import List
from adt.types.relative import Z


def test_generator():
    assert List.empty()._generator == List.empty
    assert List.cons(tail=List.empty(), head=Z.zero())._generator == List.cons


def test_constructor():
    assert List([]) == List.empty()
    assert List([-1, 0, 1]) == List.cons(
        tail=List.cons(
            tail=List.cons(
                tail=List.empty(),
                head=Z(-1)),
            head=Z(0)),
        head=Z(1))


def test_add_():
    assert List([]) + List([]) == List.empty()
    assert List([]) + List([1]) == List([1])
    assert List([1]) + List([]) == List([1])
    assert List([-1]) + List([0]) == List.cons(
        tail=List.cons(
            tail=List.empty(),
            head=Z(-1)),
        head=Z(0))

    assert List([-1]) + List([0, 1]) == List.cons(
        tail=List.cons(
            tail=List.cons(
                tail=List.empty(),
                head=Z(-1)),
            head=Z(0)),
        head=Z(1))


def test_str_():
    assert List([]).__str__() == 'List()'
    assert List([-1, 0, 1]).__str__() == 'List(Z(-Nat(1)),Z(Nat(0)),Z(Nat(1)))'


def test_pop():
    assert List([-1, 0, 1]).pop() == (List([-1, 0]), Z(1))
    assert List([]).pop() == (List.empty(), List.empty())
