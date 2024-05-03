a=[1,0,0,2,3,5,0,6,7,0]
l=len(a)
j = 0
count = 0

for i in range(0,l):
    if a[(l-1)-i] != 0:
        a[(l-1)-j] = a[(l-1)-i]
        j+=1   
    else:
        count+=1      
   
for i in range(count):
    a[i] = 0

print(a)