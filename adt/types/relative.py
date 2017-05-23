from stew.core import Sort, generator, operation
from stew.matching import var

from adt.types.nat import Nat
from adt.types.bool import Bool


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
    def cons(pos: Nat, neg: Nat) -> Z:
        pass

    @operation
    def zero() -> Z:
        return Z.cons(pos=Nat(0), neg=Nat(0))

    @operation
    def __add__(self: Z, other: Z) -> Z:
        # we add pos part together and same for the neg part
        # x = self._generator_args['pos'] + other._generator_args['pos']
        # y = self._generator_args['neg'] + other._generator_args['neg']
        # we create a new number with this value
        # and we normalize
        if (self == Z.cons(pos=var.x1, neg=var.x2)) and (other == Z.cons(pos=var.y1, neg=var.y2)):
            x = var.x1 + var.y1
            y = var.x2 + var.y2
            z = Z.cons(pos=x, neg=y)
            z = z.normalize()
            return z

    @operation
    def __sub__(self: Z, other: Z) -> Z:
        # to sub we just add the inverse
        # same procedure as the add
        if (self == Z.cons(pos=var.x1, neg=var.x2)) and (other == Z.cons(pos=var.y1, neg=var.y2)):
            x = var.x1 + var.y2
            y = var.x2 + var.y1
            z = Z.cons(pos=x, neg=y)
            z = z.normalize()
            return z

    @operation
    def __gt__(self: Z, other: Z) -> Z:
        if (self == Z.cons(pos=var.x1, neg=var.x2)) and (other == Z.cons(pos=var.y1, neg=var.y2)):
            # if the pos part is greater
            # it's true
            if var.x1 > var.y1:
                return Bool.true()
            # same thing if the neg part is smaller
            elif var.x2 < var.y2:
                return Bool.true()
            else:
                return Bool.false()

    @operation
    def __lt__(self: Z, other: Z) -> Z:
        if (self == Z.cons(pos=var.x1, neg=var.x2)) and (other == Z.cons(pos=var.y1, neg=var.y2)):
            # simply the oposite of __gt__
            if var.x1 < var.y1:
                return Bool.true()
            elif var.x2 > var.y2:
                return Bool.true()
            else:
                return Bool.false()

    @operation
    def normalize(self: Z) -> Z:
        if (self == Z.cons(pos=var.x, neg=var.y)):
            # if self.x == 0 or self.y == 0
            if var.x == Nat.zero() or var.y == Nat.zero():
                return self

            # else we reduce
            elif var.x == Nat.suc(var.xx) and var.y == Nat.suc(var.yy):
                return Z.cons(pos=var.xx, neg=var.yy).normalize()

    def __str__(self):
        x = self._generator_args['pos']
        y = self._generator_args['neg']
        if x >= y:
            return '%s(%s)' % (self.__class__.__name__, x)
        else:
            return '%s(-%s)' % (self.__class__.__name__, y)
