'''n=int(input('enter n value:'))
for i in range(n+1):
    for j in range(i):
        print(j+1,end=' ')
    print()'''
        
'''n=int(input('enter n value:'))
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()'''

'''n=int(input('enter n value:'))
for i in range(n):
    for j in range(i+1):
        print(i*j,end=' ')
    print()'''

'''n=int(input('enter n value:'))
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+j),end=' ')
    print()'''

'''n=int(input('enter n value:'))
c=65
for i in range(n):
    for j in range(i+1):
        print(chr(c),end=' ')
        c+=1
    print()'''

#while loops:
'''l=[1,2,3,4,12,35,67,89]
i=0
while i<len(l):
    if l[i]==43:
        print(l[i],'found at',i)
        i+=1
        break
else:
    print('43 not found')'''

#find max value:
'''l=[1,2,3,4,12,35,67,89]
i=0
m=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)'''

#increment value in the list:
'''l=[1,2,3,4,12,35,67,89]
i=0
j=len(l)-1
res=[]
while i<=j:
    if i==j:
        res.append(l[i])
    else:
        res.append(l[i]+l[j])
        i+=1
        j-=1
print(res)'''



#List Comprehension:
#we perform iteration and updation in one line of expression:
'''l=[1,2,3,5,3,7,6]
res=[i+10 for i in l]
print(res)'''


'''l=[1,2,3,5,3,7,6]
res=[l[i]*i for i in range(len(l))]
print(res)'''


'''l=[1,2,3,5,3,7,6]
res=[i**3 for i in l]
print(res)'''

'''l=[1,2,3,5,3,7,6]
res=[i  for i in l if i%2==0]
print(res)'''

l=[1,2,3,5,3,7,6]
res=[i if i%2==0 else 0 for i in l]
print(res)
        
        
        
