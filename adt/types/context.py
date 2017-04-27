from stew.core import Sort, generator, operation
from adt.types.bool import Bool
from adt.types.string import String
from adt.types.expr import Expr
from collections import OrderedDict
from stew.matching import var


class Context(Sort):
    """ Context sort represents the list of all substitutions for a specific context"""
    pass
    # @generator
    # def empty() -> Context:
    #     pass

    # @generator
    # def add(my_context: Context, key: String, value: Expr) -> Context:
    #     return Context.add(remove_key(my_context, key), key, value)

    # @operation
    # def contains_key(my_context: Context, key: String) -> Bool:
    #     if my_context == Context.empty():
    #         return Bool.false()

    #     if my_context == Context.add(var.c, var.k, var.e):
    #         if key == var.k:
    #             return Bool.true()
    #         return contains_key(var.c, key)
    #
    # @operation
    # def remove_key(my_context: Context, key: String) -> Context:
    #     if my_context == Context.empty():
    #         return my_context

    #     if my_context == Context.add(var.c, var.k, var.e):
    #         if key == var.k:
    #             return remove_key(var.c, key)
    #         return add(remove_key(var.c, key), var.k, var.e)

    # @operation
    # def get(context: Context, key: String) -> Expr:
    #     if context == Context.add(var.c, var.k, var.e):
    #         if key == var.k:
    #             return var.e
    #         return get(var.c, key)
    #     pass

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], dict):
            d = OrderedDict(sorted(args[0].items()))

            Sort.__init__(self)
            if not(d):
                self._generator = Context.empty
            else:
                key = list(d.keys())[0]
                value = d.pop(list(d.keys())[0])
                self._generator = Context.add
                self._generator_args = {'my_context': Context(d), 'key': String(key), 'value': Expr(value)}

        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Context:
        pass

    @generator
    def add(my_context: Context, key: String, value: Expr) -> Context:

        # if the map is empty, it's end
        if my_context == Context.empty():
            return Context.empty()

        # if this is an add, we check the value
        elif my_context == Context.add(my_context=var.context, key=var.key, value=var.value):
            # if the keys are equals
            if var.key == key:
                # we change the value
                return Context.add(
                    my_context=var.context,
                    key=var.key,
                    value=value)
            else:
                return Context.add(
                    my_context=var.context,
                    key=var.key,
                    value=var.value)

    @operation
    def get_value(my_context: Context, key: String) -> Expr:
        # if the map is empty , it's end
        if my_context == Context.empty():
            return Expr.empty()

        elif my_context == Context.add(my_context=var.context, key=var.key, value=var.value):
            # if the keys are equals we return the value
            if var.key == key:
                return var.value
            # we juste continue the recursive function
            return (var.context).get_value(key)

    @operation
    def has(my_context: Context, key: String) -> Bool:
        # same reasonnement as get_value,
        # but we return true/false instead of value
        # if the map is empty , it's end
        if my_context == Context.empty():
            return Bool.false()

        elif my_context == Context.add(my_context=var.context, key=var.key, value=var.value):
            if var.key == key:
                return Bool.true()

            return (var.context).has(key)

    @operation
    def remove(my_context: Context, key: String) -> Context:
        # we build a map without the given key
        # if the map is empty, it's end
        if my_context == Context.empty():
            return Context.empty()

        # if this is an add, we check the value
        elif my_context == Context.add(my_context=var.context, key=var.key, value=var.value):
            if var.key == key:
                return (var.context).remove(key)
            else:
                return Context.add(
                    my_context=(var.context).remove(key),
                    key=var.key,
                    value=var.value)

    def _as_dict(self):
        if self._generator == Context.empty:
            return ''
        elif self._generator == Context.add:
            if self._generator_args['my_context'] == Context.empty():
                return str(self._generator_args['key']) + ":" + str(self._generator_args['value'])
            else:
                return str(self._generator_args['key']) + ":" + str(self._generator_args['value']) + ", " + self._generator_args['my_context']._as_dict()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_dict())
