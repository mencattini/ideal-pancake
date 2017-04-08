from relative import Z
from stew.core import Sort, generator, operation


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
                self._generator_args = {'self': Map(d), 'key': Z(key), 'value': Z(value)}

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Map: pass

    @generator
    def add(self: Map, key: Z, value: Z) -> Map:

        # if the map is empty, it's end
        if self._generator == Map.empty():
            return Map.empty()

        # if this is an add, we check the value
        elif self._generator == Map.add:
            inside_key = self._generator_args['key']

            if inside_key == key:
                self._generator_args['value'] = value

            return Map.add(self=self._generator_args['self'], key=inside_key, value=self._generator_args['value'])

    @operation
    def remove(self: Map, key: Z) -> Map:

        # if the map is empty, it's end
        if self._generator == Map.empty():
            return Map.empty()

        # if this is an add, we check the value
        elif self._generator == Map.add:
            inside_key = self._generator_args['key']

            if inside_key == key:
                return self._generator_args['self'].remove(key)

            return Map.add(self=self._generator_args['self'].remove(key), key=inside_key, value=self._generator_args['value'])

    def _as_dict(self):
        if self._generator == Map.empty:
            return ''
        elif self._generator == Map.add:
            if self._generator_args['self'] == Map.empty():
                return str(self._generator_args['key']) + ":" + str(self._generator_args['value'])
            else:
                return self._generator_args['self']._as_dict() + ", " + str(self._generator_args['key']) + ":" + str(self._generator_args['value'])

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_dict())
