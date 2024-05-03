a=[0,1,0,0,2,3,5,4,0,5,0,6,0]
l=len(a)
j=0
count = 0
for i in range(0,l):
    if a[i] != 0:
        a[j] = a[i]
        j+=1
    else:
        count+=1
for i in range(count):
    a[(l-1)-i] = 0
print(a)