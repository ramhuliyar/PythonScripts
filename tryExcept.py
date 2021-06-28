try:
    with open('Hello.txt') as f:
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Raised Exception')
else:
    print(f.read())
    f.close()
finally:
    print('Try Except finally block')

