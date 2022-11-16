s=int(input())
b=int(input())
i=0
j=1
for i in range(s):
    i=i+j
    if i==b:
        i=i-j
        j+=1
    else:
        j+=1
        
print(i)        
