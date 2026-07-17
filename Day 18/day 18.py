#generate factors of a number:
'''def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
def gen(res):
    for i in res:
        yield i

n=factors(24)
g=gen(n)
for i in range(len(n)):
        print(next(g))'''


#generate even numbers from a list of numbers:

'''def even(l):
    return list(filter(lambda i:i%2==0,l ))

def gen(l):
    for i in l:
        yield i

l=[1,4,2,6,5,4,3,6,3]
e=even(l)
g=gen(e)
for i in range(len(e)):
    print(next(g))'''

#count digits using recursion:
'''def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
print(count(123456))'''

#power of a number:
def pow(n,b):
    if b==1:
        return 1
    return ns*pow(n,b-1)
print(pow(10,2))



