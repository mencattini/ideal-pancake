from stew.core import Sort, generator


class Unary_op(Sort):
    """Operation sort represents a basic python operation
    taking only one argument"""

    @generator
    def o_not() -> Unary_op:
        pass

    # Take the opposite of a relative number
    @generator
    def uSub() -> Unary_op:
        pass
