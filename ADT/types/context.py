from stew.core import Sort, generator, operation

from ADT.types.bool import Bool
from ADT.types.string import String



''' Context sort represents the list of all substitutions for a specific context'''
class Context(Sort):

    @generator
    def empty() -> Context:
        pass

    @generator
    def add(my_context: Context, key: String, value: Expr) -> Context:
        return add(remove_key(my_context), key, value)


    @operation
    def contains_key(my_context: Context, key: String) -> Bool:
        if my_context == Context.empty():
            return Bool.false()
        
        if my_context == Context.add(var.c, var.k, var.e):
            if key == var.k:
                return Bool.true()
            return contains_key(var.c, key)


    @operation
    def remove_key(my_context: Context, key: String) -> Context:
        if my_context == Context.empty():
            return my_context

        if my_context == Context.add(var.c, var.k, var.e):
            if key == var.k:
                return remove_key(var.c, key)
            return add(remove_key(var.c, key), var.k, var.e)
    

