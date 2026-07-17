#lambda functions:
'''add=lambda a,b:a+b
print(add(2,4))'''

'''pow=lambda a,b:a**b
print(pow(2,4))'''

'''wish =lambda name:f'{name},welcome'
print(wish('sreeja'))'''

'''even_odd=lambda n:'even' if n%2==0 else 'odd'
print(even_odd(15))'''

'''square=lambda n:n**2
print(square(2))'''

'''
check=lambda a,b:max(a,b)
print(check(15,19))'''

'''check=lambda a,b:a if a>b else b
print(check(15,19))'''

'''check=lambda str:len(str)
print(check('sreeja'))'''

'''check=lambda str:'starts with vow' if str[0] in 'aeiouAEIOU' else 'starts with cons'
print(check('sreeja'))'''

#extract domain of an email:
'''check=lambda email:email.split('@')[-1]
print(check('sreeja@gmail.com'))'''

#leap year:
'''check= lambda year:'leap year' if year%400==0 or(year%4==0 and year%100!=0) else 'non leap year'
print(check(2004))
print(check(2026))'''

#last digit:
'''check=lambda n:n%10
print(check(234))'''

#sequence of elements:(list,tuple,dict.set):
'''l=[1,2,3,1,2,3]
square=list(map(lambda i:i**2 ,l))
print(square)'''

'''l=['sreeja','vanga']
res=list(map(lambda i:i.upper(),l))
print(res)'''

'''l=[1,2,3,1,2,3]
res=list(map(lambda i:i+10,l))
print(res)'''

#sorting dict,list,set using lambda:
d={'sreeja':95,'vanga':90,'bhavya':91}
res=dict(sorted(d.items(),key=lambda i:i[1]))#as it prints as tuple where 0 index refers to keys and 1 index refers to values
print(res)
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))
