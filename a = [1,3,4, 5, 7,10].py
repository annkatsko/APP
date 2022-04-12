a = [1,3,4, 5, 7,10]
z=[]
h=[]
for g in range(1,max(a)):
    z.append(g)
z.append(a[-1])
for i in z:
     if i not in a:
         h.append(i)
print(h)