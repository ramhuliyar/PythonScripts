def getMethods(object):
    methods = [method for method in dir(object) if callable(getattr(object,method))]
    regularMethods = []
    for method in methods:
        if '__' not in method:
            regularMethods.append(method)

    return regularMethods
            

print(getMethods(dict))

