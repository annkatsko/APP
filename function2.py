from re import I


def func(a, b):
    s=[]
    i = 0
    while i!=len(a) and i!=len(b):
        for j in a:
            if j in b:
                s+=j
                break
        i+=1

    print(*s)

    
func('daaa', 'daaaa')