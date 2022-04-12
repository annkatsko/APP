a = [1,3,4, 5, 7,10]
z=[]
h=[]
for g in range(a[0], a[-1]):
    z.append(g)
z.append(a[-1])
print(z)
for i in a:
   if a[i]!=z[i]:
        h.append(z[i])
        break


