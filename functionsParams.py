def ask_ok(prompt='Do you really want to quit?', retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


print(ask_ok(prompt='Do you really want to QUIT?'))

def foo(a, L=[]):
    L.append(a)
    return L

for i in range(4):
    print(foo(i))


def foo(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

for i in range(4):
    print(foo(i))


