from ADT.types.map import Map
from ADT.types.relative import Z
from ADT.types.bool import Bool
from ADT.types.relative_list import List


def test_generator():
    assert Map.empty()._generator == Map.empty
    assert Map.add(my_map=Map.empty(), key=Z.zero(), value=Z.zero())._generator == Map.add


def test_constructor():
    assert Map({}) == Map.empty()
    assert Map({1: 1}) == Map.add(my_map=Map.empty(), key=Z(1), value=Z(1))
    assert Map({1: 1, -2: -2}) == Map.add(
        my_map=Map.add(my_map=Map.empty(), key=Z(-2), value=Z(-2)),
        key=Z(1),
        value=Z(1))


def test_get_value():
    my_map = Map({1: 1, -2: -2, 0: 0})
    assert my_map.get_value(Z(1)) == Z(1)
    assert my_map.get_value(Z(-2)) == Z(-2)
    assert my_map.get_value(Z(-3)) == Map.empty()


def test_has():
    my_map = Map({1: 1, -2: -2, 0: 0})
    assert my_map.has(Z(1)) == Bool.true()
    assert my_map.has(Z(-2)) == Bool.true()
    assert my_map.has(Z(-200)) == Bool.false()

    assert Map.empty().has(Z(-200)) == Bool.false()


def test_remove():
    my_map = Map({1: 1, -2: -2, 0: 0})
    assert not(my_map.remove(Z(1)) == my_map)

    assert my_map.remove(Z(1)) == Map({-2: -2, 0: 0})
    assert my_map.remove(Z(100)) == my_map

    assert Map.empty().remove(Z(10)) == Map.empty()


def test_str_():
    assert Map.empty().__str__() == 'Map()'
    assert Map({1: 1, -2: -2}).__str__() == 'Map(Z(Nat(1)):Z(Nat(1)), Z(-Nat(2)):Z(-Nat(2)))'


def test_keys():
    assert Map({1: 1, -2: -2}).keys() == List([1, -2])
    assert Map({}).keys() == List.empty()
