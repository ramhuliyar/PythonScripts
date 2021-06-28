def move(f,t) :
    print('Move from {} to {}!'.format(f, t))

def moveVia(f,v,t) :
    move(f,v)
    move(v,t)

moveVia('A','B','C')

def hanoi(n,f,h,t) :
    if n == 0 :
        return
    else :
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(3,'A','B','C')            
