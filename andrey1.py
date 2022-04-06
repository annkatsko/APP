a = [1,1,2,2,4,5,3,3,4,7,7]
z = 1
i=0
while i+1<len(a):
  if a[i]==a[i+1]:
    z+=1
  else:
   print(str(a[i]) + '-' + str(z))
   z=1
  i=i+1
print(str(a[-1]) + '-' + str(z))