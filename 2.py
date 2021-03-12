d={}                                                #d is a dict where we store product_name:[quantity,price,unit]
budget=int(input('Enter Your budget:- ')) 
while True:
    if budget>0:
        print('1.Add an item')
        print('2.Exit')
        option=int(input('Enter your choice : '))
        if option==1:
            prod=input('Enter Product: ')
            quantity=input('Enter quantity :').split(' ')
            qty=float(quantity[0])
            unit=quantity[1]
            price=int(input('Enter Price: '))
            try:                                      #we check wheather the product_name is already present in dict if so try will execute successfully
                update=d[prod]
                temp=price
                amount=d[prod][1]-price+budget
                if amount>=0:
                    d[prod][0]=qty
                    price=d[prod][1]-price
                    d[prod][1]=temp
                    d[prod][2]=unit
                    budget=amount
                    print('Amount left :'+str(amount))
                else:
                    print("Can't Buy the product ###(because budget left is "+str(budget)+" )")   #if budget is less than the cost of the item
            except:                                                             #if the dict don't have the product
                if budget-price>=0:
                    d[prod]=[qty,price,unit]
                    budget-=price
                    print('Amount left :'+str(budget))
                else:
                    print("Can't Buy the product ###(because budget left is "+str(budget)+" )")      #if budget is less than the cost of the item
        else:
            break
    else:
        break
        
        
for key in d.keys():
    if d[key][1]==budget:
        print('Amount left can buy you ' + key)
print('\n')
print('GROCERY LIST is:')
print("Product name    Quantity    Price")
for key in d.keys():
      print(key+"        "+(10-len(key))*" "+str(d[key][0])+str(d[key][2])+"     "+str(d[key][1]))
            
            
