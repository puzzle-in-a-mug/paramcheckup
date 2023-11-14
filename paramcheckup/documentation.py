### FUNCTIONS ###


def docstring_parameter(*args, **kwargs):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*args, **kwargs)
        return obj

    return dec


### CONSTANTS ###


ALPHA = {
    "type": "alpha : float, optional",
    "description": "The level of significance (:math:`\\alpha`). Default is ``0.05``;",
}


# PARAM = {
#     "type":
#     "description":
# }
