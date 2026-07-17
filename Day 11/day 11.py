#patterns:


'''n=int(input('enter the size:'))
for i in range(n):#loop for rows
    for j in range(n):#loop for cols
        print('*',end=' ')
    print()'''

# to print right angled triangle:
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')

    print()'''

#to print inverted right angled triangle:
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')

    print()'''

#to print reverse right angled triangle:
'''n=int(input('enter the size:'))
for i in range(n):
    for k in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()'''

#to print inverted left angled triangle
'''n=int(input('enter the size:'))
for i in range(n):
    for k in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()'''

#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        print(int(j%2==0),end=' ')
    print()'''

#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        print(int(not j%2==0),end=' ')
    print()'''

#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        print(int((i+j)%2==0),end=' ')
    print()'''
#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        print(int(not (i+j)%2==0),end=' ')
    print()'''

#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or n//2==i or n//2==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#
''''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (i+j)==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#
'''n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if (i+j)==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
#
n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
