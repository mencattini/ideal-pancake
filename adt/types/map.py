from adt.types.relative import Z
from stew.core import Sort, generator, operation
from stew.matching import var
from adt.types.bool import Bool
from adt.types.relative_list import List


class Map(Sort):

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], dict):
            d = args[0]

            Sort.__init__(self)
            if not(d):
                self._generator = Map.empty
            else:
                key = list(d.keys())[0]
                value = d.pop(list(d.keys())[0])
                self._generator = Map.add
                self._generator_args = {
                    'my_map': Map(d),
                    'key': Z(key),
                    'value': Z(value)
                    }

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Map:
        pass

    @generator
    def add(my_map: Map, key: Z, value: Z) -> Map:

        # if the map is empty, it's end
        if my_map == Map.empty():
            return Map.empty()

        # if this is an add, we check the value
        elif my_map == Map.add(my_map=var.map, key=var.key, value=var.value):
            # if the keys are equals
            if var.key == key:
                # we change the value
                return Map.add(
                    my_map=var.map,
                    key=var.key,
                    value=value)
            else:
                return Map.add(
                    my_map=var.map,
                    key=var.key,
                    value=var.value)

    @operation
    def get_value(my_map: Map, key: Z) -> Map:
        # if the map is empty , it's end
        if my_map == Map.empty():
            return Map.empty()

        elif my_map == Map.add(my_map=var.map, key=var.key, value=var.value):
            # if the keys are equals we return the value
            if var.key == key:
                return var.value
            # we juste continue the recursive function
            return (var.map).get_value(key)

    @operation
    def has(my_map: Map, key: Z) -> Map:
        # same reasonnement as get_value,
        # but we return true/false instead of value
        # if the map is empty , it's end
        if my_map == Map.empty():
            return Bool.false()

        elif my_map == Map.add(my_map=var.map, key=var.key, value=var.value):
            if var.key == key:
                return Bool.true()

            return (var.map).has(key)

    @operation
    def remove(my_map: Map, key: Z) -> Map:
        # we build a map without the given key
        # if the map is empty, it's end
        if my_map == Map.empty():
            return Map.empty()

        # if this is an add, we check the value
        elif my_map == Map.add(my_map=var.map, key=var.key, value=var.value):
            if var.key == key:
                return (var.map).remove(key)
            else:
                return Map.add(
                    my_map=(var.map).remove(key),
                    key=var.key,
                    value=var.value)

    @operation
    def keys(my_map: Map) -> List:
        if my_map == Map.empty():
            return List.empty()

        elif my_map == Map.add(my_map=var.map, key=var.key, value=var.value):
            list_tmp = List.cons(tail=List.empty(), head=var.key)
            return list_tmp + (var.map).keys()

    def _as_dict(self):
        if self._generator == Map.empty:
            return ''
        elif self._generator == Map.add:
            if self._generator_args['my_map'] == Map.empty():
                return (
                    str(self._generator_args['key'])
                    + ":" + str(self._generator_args['value'])
                    )
            else:
                return (
                    str(self._generator_args['key']) + ":" +
                    str(self._generator_args['value']) + ", " +
                    self._generator_args['my_map']._as_dict()
                    )

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_dict())
