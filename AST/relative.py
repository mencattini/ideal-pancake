from stew.core import Sort, generator, operation
from stew.matching import var

from nat import Nat
from bool import Bool


class Z(Sort):
    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], int):
            number = args[0]

            Sort.__init__(self)
            if number == 0:
                self._generator = Z.cons
                self._generator_args = {'pos': Nat.zero(), 'neg': Nat.zero()}
            elif number > 0:
                self._generator = Z.cons
                self._generator_args = {'pos': Nat(number), 'neg': Nat.zero()}
            else:
                self._generator = Z.cons
                self._generator_args = {'pos': Nat.zero(), 'neg': Nat(-number)}

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def zero() -> Z: pass

    @generator
    def cons(pos: Nat, neg: Nat) -> Z: pass

    @operation
    def __add__(self: Z, other: Z) -> Z:
        x = self._generator_args['pos'] + other._generator_args['pos']
        y = self._generator_args['neg'] + other._generator_args['neg']
        z = Z.cons(pos=x, neg=y)
        z.normalize()
        return z

    @operation
    def __eq__(self: Z, other: Z) -> Z:
        x = self._generator_args
        y = other._generator_args
        if x['pos'] == y['pos'] and x['neg'] == y['neg']:
            return Bool.true()
        return Bool.false()

    @operation
    def __gt__(self: Z, other: Z) -> Z:
        x = self._generator_args
        y = other._generator_args
        if x['pos'] > y['pos']:
            return Bool.true()
        elif x['neg'] < y['neg']:
            return Bool.true()
        else:
            return Bool.false()

    @operation
    def __lt__(self: Z, other: Z) -> Z:
        x = self._generator_args
        y = other._generator_args
        if x['pos'] < y['pos']:
            return Bool.true()
        elif x['neg'] > y['neg']:
            return Bool.true()
        else:
            return Bool.false()

    @operation
    def normalize(self: Z) -> Z:

        x = self._generator_args['pos']
        y = self._generator_args['neg']

        # if self.x == 0 or self.y == 0
        if x == Nat.zero() or y == Nat.zero():
            return self

        # else we reduce
        elif x == Nat.suc(var.xx) and y == Nat.suc(var.yy):
            self._generator_args['pos'] = var.xx
            self._generator_args['neg'] = var.yy
            return self.normalize()

    def __str__(self):
        x = self._generator_args['pos']
        y = self._generator_args['neg']
        if x >= y:
            return '%s(%s)' % (self.__class__.__name__, x)
        else:
            return '%s(-%s)' % (self.__class__.__name__, y)
