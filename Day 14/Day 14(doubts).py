#accesing the dict:
'''products={'salt':{'stock':20,'discount':50,'price':100},
          'milk':{'stock':0,'discount':0,'price':200},
          'sugar':{'stock':10,'discount':10,'price':300},
          }
for i in products:
    if products[i]['stock']:
        print(i)'''


#to print sum of price:
products={'salt':{'stock':20,'discount':50,'price':100},
          'milk':{'stock':0,'discount':0,'price':200},
          'sugar':{'stock':10,'discount':10,'price':300},
          }
for i in products:
        if products[i]['stock']:
            price=products[i]['price']
            print(
