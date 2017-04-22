from ADT.types.relative import Z
from stew.core import Sort, generator, operation

from ADT.types.bool import Bool
from ADT.types.relative_list import List
from ADT.types.expr_list import Expr_list


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
                self._generator_args = {'my_map': Map(d), 'key': Z(key), 'value': Z(value)}

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Map: 
        pass

    @generator
    def add(my_map: Map, key: Z, value: Z) -> Map:

        # if the map is empty, it's end
        if my_map._generator == Map.empty():
            return Map.empty()

        # if this is an add, we check the value
        elif my_map._generator == Map.add:
            inside_key = my_map._generator_args['key']

            # if the keys are equals
            if inside_key == key:
                # we change the value
                my_map._generator_args['value'] = value

            return Map.add(my_map=my_map._generator_args['my_map'], key=inside_key, value=my_map._generator_args['value'])

    #Possibility to call a function in a Map term
    @generator
    def func(e_list: Expr_list) -> Map:
        pass

    @operation
    def get_value(my_map: Map, key: Z) -> Map:
        # if the map is empty , it's end
        if my_map._generator == Map.empty:
            return Map.empty()

        elif my_map._generator == Map.add:
            inside_key = my_map._generator_args['key']
            # if the keys are equals we return the value
            if inside_key == key:
                return my_map._generator_args['value']
            # we juste continue the recursive function
            return my_map._generator_args['my_map'].get_value(key)

    @operation
    def has(my_map: Map, key: Z) -> Map:
        # same reasonnement as get_value,
        # but we return true/false instead of value
        # if the map is empty , it's end
        if my_map._generator == Map.empty:
            return Bool.false()

        elif my_map._generator == Map.add:
            inside_key = my_map._generator_args['key']

            if inside_key == key:
                return Bool.true()

            return my_map._generator_args['my_map'].has(key)

    @operation
    def remove(my_map: Map, key: Z) -> Map:
        # we build a map without the given key
        # if the map is empty, it's end
        if my_map._generator == Map.empty:
            return Map.empty()

        # if this is an add, we check the value
        elif my_map._generator == Map.add:
            inside_key = my_map._generator_args['key']

            if inside_key == key:
                return my_map._generator_args['my_map'].remove(key)
            else:
                return Map.add(my_map=my_map._generator_args['my_map'].remove(key), key=inside_key, value=my_map._generator_args['value'])

    @operation
    def keys(my_map: Map) -> List:
        if my_map._generator == Map.empty:
            return List.empty()

        elif my_map._generator == Map.add:
            list_tmp = List.cons(tail=List.empty(), head=my_map._generator_args['key'])
            return list_tmp + my_map._generator_args['my_map'].keys()

    def _as_dict(self):
        if self._generator == Map.empty:
            return ''
        elif self._generator == Map.add:
            if self._generator_args['my_map'] == Map.empty():
                return str(self._generator_args['key']) + ":" + str(self._generator_args['value'])
            else:
                return str(self._generator_args['key']) + ":" + str(self._generator_args['value']) + ", " + self._generator_args['my_map']._as_dict()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_dict())
