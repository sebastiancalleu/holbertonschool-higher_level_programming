#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        new = fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as er:
        print("Exception:", er, file=sys.stderr)
        return (None)
    return (new)