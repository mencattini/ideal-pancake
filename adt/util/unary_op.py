from stew.core import Sort, generator, operation
from sew.matching import var

class Unary_Op(Sort):
    """Operation sort represents a basic python operation taking only one argument"""

    @generator
    def not() -> Unary_Op:
        pass

    # Take the opposite of a relative number
    @generator
    def uSub() -> Unary_op:
        pass
