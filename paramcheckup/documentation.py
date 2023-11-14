### FUNCTIONS ###


def docstring_parameter(*args, **kwargs):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*args, **kwargs)
        return obj

    return dec


### CONSTANTS ###


NUMBER = {
    "type": "number : int or float",
    "description": "The number that needs to be checked;",
}

LOWER = {
    "type": "lower : int or float",
    "description": "The lower bound;",
}


UPPER = {
    "type": "upper : int or float",
    "description": "The upper bound;",
}

PARAM_NAME = {
    "type": "param_name : str",
    "description": "The name of the parameter that received the variable ",
}

KIND = {
    "type": "kind : str",
    "description": "The object where `param_name` is applied (function, method, class, etc.);",
}

KIND_NAME = {"type": "kind_name : str", "description": "The name of the object `kind`;"}


INCLUSIVE = {
    "type": "inclusive : bool, optional",
    "description": "Specify whether the boundaries should be open (`False`) or closed (`True`, default);",
}


STACKLEVEL = {
    "type": "stacklevel : int, optional",
    "description": "The stacking level (default is ``4``);",
}

ERROR = {
    "type": "error : bool, optional",
    "description": "Whether to display error text (`True`, default) or not (`False`);",
}


# PARAM = {
#     "type":
#     "description":
# }
