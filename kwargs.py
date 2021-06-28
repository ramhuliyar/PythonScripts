def foo(first, *args, **kwargs):
    print(first)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print('In kwargs', kwargs[kwarg])
        

foo('hello1', 1, 2, 3, one=1, two= 2)

'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")        
'''
