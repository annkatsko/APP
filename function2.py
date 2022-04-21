def func(a, b):
    s=[]
    i = 0
    while i!=len(a) and i!=len(b):
        if a[i] in b:
            s+=a[i]
        i+=1

    print(*s)

    
func('daaa', 'daaaa')