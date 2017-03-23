from stew.core import Sort, generator, operation


class Liste(Sort):

    def __init__(self, *args, **kwargs):
        if(len(args) == 1) and isinstance(args[0], list):
            Sort.__init__(self)
            if len(args[0]) == 0:
                self._generator = Liste.empty
            else:
                self._generator = Liste.add
                self._generator_args = {'self': Liste(args[0][:-1]), 'other': args[0][-1]}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Liste:
        pass

    @generator
    def add(self: Liste, other: Sort) -> Liste:
        pass
