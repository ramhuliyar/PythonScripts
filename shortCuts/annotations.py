def validate(func, locals):
    for var, test in func.__annotations__.items():
        value = locals[var]
        try:
            print(test)
            print(test.__name__)
            print(test.__docstring__)
            pr=test.__name__+': '+test.__docstring__
            print(pr)
        except AttributeError:
            pr=test.__name__   
        msg = '{}=={}; Test: {}'.format(var, value, pr)
        assert test(value), msg

def between(lo, hi):
    def _between(x):
            return lo <= x <= hi
    _between.__docstring__='must be between {} and {}'.format(lo,hi)       
    return _between

def f(x: between(3,10), y:lambda _y: isinstance(_y,int)):
    validate(f, locals())
    print(x,y)

print(between.__name__)
f(5, 2)
