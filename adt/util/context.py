from stew.core import Sort, generator, operation
from stew.matching import var

from adt.types.string import String
from adt.util.literal import Literal


class Context(Sort):
    """ Context sort represents the list of all substitutions for a specific context"""
    

    @generator
    def empty() -> Context:
        pass

    @generator
    def cons(c: Context, k: String, v: Literal) -> Context:
        pass

    @operation
    def add(c: Context, k: String, v: Literal) -> Context:
        if c == Context.empty():
            return Context.cons(c=c, k=k, v=v)

    
        if c == Context.cons(c=var.context, k=var.key, v=var.value):
            if k == var.key:
                return Context.cons(c=var.context, k=var.key, v=v)
            else:
                return Context.cons(c=Context.add(c=var.context, k=k, v=v), k=var.key, v=var.value)


    @operation
    def get_value(c: Context, k: String) -> Literal:
        if c == Context.cons(c=var.context, k=var.key, v=var.value):
            if k == var.key:
                return var.value
            else:
                return Context.get_value(c=var.context, k=k, v=v)
            
    @operation
    def remove(c: Context, k: String) -> Context:
        if c == Context.empty():
            return c
        if c == Context.cons(c=var.context, k=var.key, v=var.value):
            if k == var.key:
                return var.context
            else:
                return Context.cons(c=Context.remove(c=var.context, k=k), k=var.key, v=var.value) 

