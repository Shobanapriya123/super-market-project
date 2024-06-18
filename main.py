import item_lists

try:
    print("first floor-> grocerries to press 1")
    print("second floor-> stationary products to press 2")
    print("third floor-> food court to press 3")
    print("fourth floor-> dresses to press 4")
    print("fifth floor-> cheppals to press 5")    
    
    user=int(input("enter your floor number:"))
    if user==1:
        item_lists.grocerries()
    elif user==2:
        item_lists.stationary_products()
    elif user==3:
        item_lists.food_court()
    elif user==4:
        item_lists.dresses()
    elif user==5:
        item_lists.cheppals()
        
    else:
        print("this item is not available")
        
except:
    print("pls typr crt number")
    
                
    
        
    