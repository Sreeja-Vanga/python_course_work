#to remove 0's from the list:
'''l=[0,1,2,0,8,0,6,0,8,0]
while 0 in l:
    l.remove(0)
print(l)'''

#to print 1 to 10 numbers using while loop:
'''i=1
while i<=10:
    print(i)
    i+=1'''

#to print 100 to 2 numbers using while loop:
'''i=100
while i>=2:
    print(i)
    i-=1'''

#to print a table:
'''n=int(input('enter the value:'))
i=1
while i<=10:
    print(f'{n}*{i}={n*i}')
    i+=1'''

#print sum of digits of a number:
'''n=int(input('enter the number:'))
s=0
while n>0:
    r=n%10
    s+=r
    n//=10
print(s)'''

#factorial:
'''n=int(input('enter the number:'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

#factors of a number:
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    if n%i==0:
        print(i)'''

#to print next alpha in a word:
'''word=input('enter the word:')
res=''
for ch in word:
    res+=chr(ord(ch)+1)
print(res)'''

#to print reverse index order of a word:
'''word=input('enter the word:')
i=len(word)-1
while i>=0:
    print(word[i],i)
    i-=1'''

#print first non repeating char:
'''word=input('enter the word:')
for i in word:
    if word.count(i)==1:
        print(i)
        break
else:
    print('there is no non repeating char')'''

# reverse of a number:
n=int(input('enter a number:'))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n//=10
print(rev)
    
    
    
