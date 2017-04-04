from stew.core import Sort, generator, operation
from stew.matching import var


class Z(Sort):
    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], int):
            number = args[0]

            Sort.__init__(self)
            if number == 0:
                self._generator = Z.zero
            elif number > 0:
                self._generator = Z.suc
                self._generator_args = {'main': Z(number - 1)}
            else:
                self._generator = Z.pre
                self._generator_args = {'main': Z(number + 1)}

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def zero() -> Z: pass

    @generator
    def suc(main: Z) -> Z: pass

    @generator
    def pre(main: Z) -> Z: pass

    @operation
    def __add__(main: Z, other: Z) -> Z:
        # zero + y = y
        if main == Z.zero():
            return other

        # suc(x) + y = suc(x + y)
        if main == Z.suc(var.x):
            return Z.suc(var.x + other)

        # pre(x) + y = pre(x + y)
        if main == Z.pre(var.x):
            return Z.pre(var.x + other)

    @operation
    def inverse(main: Z) -> Z:
        # if suc we use pre
        if main == Z.suc(var.x):
            return Z.pre(var.x.inverse())
        # if pre we use suc
        if main == Z.pre(var.x):
            return Z.suc(var.x.inverse())
        # if zero then end
        if main == Z.zero():
            return Z.zero()

    @operation
    def __sub__(main: Z, other: Z) -> Z:
        # zero - y = -y
        if main == Z.zero():
            return other.inverse()

        # x - zero = x
        if other == Z.zero():
            return main

        # suc(x) - y = x - pre(y)
        if main == Z.suc(var.x):
            return var.x - Z.pre(other)

        # pre(x) - y = x - suc(y)
        if main == Z.pre(var.x):
            return var.x - Z.suc(other)

    def _as_int(self):
        if self._generator == Z.zero:
            return 0
        elif self._generator == Z.suc:
            return 1 + self._generator_args['main']._as_int()
        elif self._generator == Z.pre:
            return self._generator_args['main']._as_int() - 1

    def __str__(self):
        return '%s(%i)' % (self.__class__.__name__, self._as_int())
