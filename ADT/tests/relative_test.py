from ADT.types.relative import Z
from ADT.types.nat import Nat
from ADT.types.bool import Bool


def test_generator():
    # because the Z.zero == Z.cons(pos=Nat(0), neg=Nat(0))
    assert Z.zero()._generator == Z.cons
    assert Z.cons(pos=Nat(0), neg=Nat(0))._generator == Z.cons


def test_constructor():
    assert Z(0) == Z.cons(pos=Nat(0), neg=Nat(0))
    assert Z(1) == Z.cons(pos=Nat(1), neg=Nat(0))
    assert Z(-1) == Z.cons(pos=Nat(0), neg=Nat(1))


def test_add_():
    assert Z(0) + Z(0) == Z(0)
    assert Z(1) + Z(0) == Z(1)
    assert Z(0) + Z(-1) == Z(-1)


def test_sub_():
    assert Z(0) - Z(0) == Z(0)
    assert Z(1) - Z(0) == Z(1)
    assert Z(0) - Z(-1) == Z(1)
    assert Z(0) - Z(1) == Z(-1)


def test_eq_():
    assert Z(0).__eq__(Z(0)) == Bool.true()
    assert Z(0).__eq__(Z(1)) == Bool.false()


def test_gt_():
    assert Z(1).__gt__(Z(0)) == Bool.true()
    assert Z(1).__gt__(Z(-1)) == Bool.true()
    assert Z(-1).__gt__(Z(-2)) == Bool.true()

    assert Z(0).__gt__(Z(0)) == Bool.false()
    assert Z(-1).__gt__(Z(-1)) == Bool.false()


def test_lt_():
    assert Z(1).__lt__(Z(0)) == Bool.false()
    assert Z(1).__lt__(Z(-1)) == Bool.false()
    assert Z(-1).__lt__(Z(-2)) == Bool.false()

    assert Z(0).__lt__(Z(0)) == Bool.false()
    assert Z(-1).__lt__(Z(-1)) == Bool.false()


def test_normalize():
    # this should be 0
    z = Z.cons(pos=Nat(1), neg=Nat(1))
    # we normalize it
    assert z.normalize() == Z(0)

    z = Z.cons(pos=Nat(1), neg=Nat(0))
    assert z.normalize() == Z(1)

    z = Z.cons(pos=Nat(0), neg=Nat(1))
    assert z.normalize() == Z(-1)


def test_str_():
    assert Z(0).__str__() == 'Z(Nat(0))'
    assert Z(1).__str__() == 'Z(Nat(1))'
    assert Z(-1).__str__() == 'Z(-Nat(1))'
