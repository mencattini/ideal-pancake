from stew.core import Sort, Attribute, generator, operation
from stew.matching import var

from adt.types.bool import Bool
from adt.types.string import String
from adt.util.block import Block


class String_list(Sort):
    """ String_list sort represents the list of parameters name of a function"""
"""
    @generator
    def empty() -> String_list:
        pass

    @generator
    def cons(tail: String_list, head: String) -> String_list:
        pass

    @operation
    def car(s_list: String_list) -> String:
        if s_list == String_list.cons(var.t, var.h):
            return var.h
        # No precision about car(Empty)
        pass

    @operation
    def cdr(s_list: String_list) -> String_list:
        if s_list == String_list_cons(var.t, var.h):
            return var.t
        # No precision about cdr(Empty)
        pass
"""

class Func(Sort):
    """ Func sort represents a function with related name, parameters and block of code"""
"""
    name = Attribute(domain = String)
    params = Attribute(domain = String_list)
    block = Attribute(domain = Block)
"""

class Func_list(Sort):
    """ Func_list sort represents the list of existing functions"""
""" 
    @generator
    def empty() -> Func_list:
        pass
    
    @generator
    def cons(tail: Func_list, head: Func) -> Func_list:
        pass

    @operation
    def car(f_list: Func_list) -> Func:
        if f_list == Func_list.cons(var.t, var.h):
            return var.h
        # No precision about car(Empty)
        pass

    @operation
    def cdr(f_list: Func_list) -> Func_list:
        if f_list == Func_list.cons(var.t, var.h):
            return var.t
        # No precision about car(Empty)
        pass

    @operation
    def get(f_list: Func_list, key: String) -> Func:
        if f_list == Func_list.cons(var.t, var.h):
            if key = var.h.name:
                return var.h
            return Func_list.get(var.t, key)
        pass

"""





