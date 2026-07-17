#lambda function with filter():
#filter is used to filter values based on the condition:(size varies before and after list , where as map, size of the list is same)
'''l=[1,2,3,4,5,6,123,45,632]
res=list(filter(lambda i:i%2==0,l))
print(res)'''

'''l='python programming'
res=list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)'''

'''l=['operators','control','sreeja','apple']
res=list(filter(lambda i:i[0] in 'aeiouAEIOU',l))
print(res)'''

'''l=['operators','control','sreeja','apple']
res=list(filter(lambda i:i[0] not in 'aeiouAEIOU',l))
print(res)'''


'''l=['operators','control','sreeja','apple']
res=list(filter(lambda i:len(i)<7,l))
print(res)'''



'''data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':55},
    'mac':{'stock':8,'price':90}}
res=list(filter(lambda i:data[i]['stock']==0,data))
print(res)'''
    
'''data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':45000},
    'mac':{'stock':8,'price':90000}}
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)'''


'''data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':45000},
    'mac':{'stock':8,'price':90000}}
res={i:data[i]['price'] for i in data}
l2h=dict(sorted(res.items(),key=lambda i:i[1]))
h2l=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))
print(l2h)
prin t(h2l)'''

#reduce is used to make the list into single unit:
'''from functools import reduce
l=['operators','control','sreeja','apple']
m=[1,2,3,5,1,2,5]
s=reduce(lambda sum,i:sum+','+i,l)
ls=reduce(lambda sum,i:sum+i,m)
lp=reduce(lambda pro,i:pro*i,m)
print(s,ls,lp)'''

#generators: are a special kind of functions to generate with divisions:
#when we use a function after display the output the function is terminated , so inorder to pause the function and generate outputs in divisions we use yeild keyword:
#yeild is used to pause the function:
'''def reels():
    r=['1..100','101..200','201..300','301...400','401..500']
    for i in r:
        yield i
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))'''


def reels():
    yield '1..100'
    yield '101..200'
    yield '201..300'
    yield '301...400'
    yield '401..500'
    
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

    
