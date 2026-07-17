#count vowels,cons,spcl chars,word counts,digits :
'''def check(s):
    vc=cc=dc=sc=0
    wc=1
    vow='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vow:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
    print(f'vow count:{vc}')
    print(f'cons count:{cc}')
    print(f'digit count:{dc}')
    print(f'word count:{wc}')
    print(f'special char count:{sc}')

s=input('enter a string:')
check(s)'''

#global keyword:
'''def display():
    global num
    num+=10
    print("inside num:",num)
num=10
display()
print("outside num:",num)'''

#int,float,str,tuple-immutable(modification reflects only for inside)
#list,set,dict-mutable ( modification reflects for both inside and outside functions)
'''def display(num):
    num+=10
    print("inside num:",num)
num=10
display(num)
print("outside num:",num)'''


'''def display(num):
    num=num+[4,5]
    print("inside num:",num)
num=[1,2,3]
display(num)
print("outside num:",num)'''

'''def display(num):
    num.append(4)
    print("inside num:",num)
num=[1,2,3]
display(num)
print("outside num:",num)'''

#when we want to reflects the changes in an inner function to outer function(i.e; when there are nested functions) then we use nonloacal keyword:
'''def courses():
    course='Java'
    print('At start:',course)
    def change():
        nonlocal course
        course='Python'
        print('Changed to:',course)
    change()
    print('Final Course:',course)
courses()'''

#scope of the variable:
'''s='sreeja'
len=5
print(len)'''

#recursion:(function inside a function with modification of the parameter and with a base condition)
'''def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)'''



'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)'''



'''def display(s,i):
    if i==len(s):
        return
    print(s[i])
    display(s,i+1)
s='python'
display(s,0)'''


'''def display(s,i):
    if i==len(s)+1:
        return
    print(s[:i])
    display(s,i+1)
s='python'
display(s,1)'''

'''def display(s,i,j):
    if i==len(s)-j+1:
        return
    print(s[i:i+j])
    display(s,i+1,j)
s='python Programming'
display(s,0,4)'''

def s(n):
    if n==n+1:
        return
    s(n-1)
s(10)





