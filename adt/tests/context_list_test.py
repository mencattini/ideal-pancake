from adt.types.context_list import Context, Context_list
from adt.types.nat import Nat, Bool


def test_generator():
    assert Context_list.empty()._generator == Context_list.empty

    a = Context({'a': Bool.true()})
    assert Context_list.cons(
        tail=Context_list.empty(),
        head=a)._generator == Context_list.cons


def test_constructor():
    assert Context_list([]) == Context_list.empty()

    a = Context({'a': Bool.true()})
    b = Context({'b': Nat(10)})

    assert Context_list.cons(
        tail=Context_list.cons(
            tail=Context_list.empty(),
            head=a),
        head=b) == Context_list([a, b])


def test_car():
    assert Context_list([]).car() == Context.empty()

    a = Context({'a': Bool.true()})
    b = Context({'b': Nat(10)})

    assert Context_list([a, b]).car() == b


def test_cdr():
    assert Context_list([]).car() == Context.empty()

    a = Context({'a': Bool.true()})
    b = Context({'b': Nat(10)})

    assert Context_list([a, b]).cdr() == Context_list([a])
