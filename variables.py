''''''

var: int  # declaration (with type hint)
var = 10  # initialization
var: int = 10  # definition

_ = 1  # throwaway variable

# UNDERSCORES (leading and trailing underscores)
_var = 3  # hint: use variable locally, e.g. do not call ._var
var_ = 3  # avoid naming conflict with var
__var = 3  # 'name mangling' py will extend name, to avoid collision - can be used as 'pseudo private'
__var__ = 3  # dunder, reserved for special use __init__ , __call__ , do not use with regular var
