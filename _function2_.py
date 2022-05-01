def func(a, b):
    s = []
    for i in a:
        if i in b and i not in s:
            s.append(i)
    a1 = [i for i in a if i in s]
    b1 =[i for i in b if i in s]
    g = [(x, min(a.count(x), b.count(x))) for x in s]
    for i in g:
        print(i[0]*i[1], end='')
    




func('abbcfcccaaaaaaf', 'faafbcb')