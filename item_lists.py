import datetime

def grocerries():
    onekg_rice=40
    onekg_millets=60
    onekg_grains=80
    
    products=["rice","millets","grains"]
    
    your_order=input("which product is you want:")
    if your_order in products:
        print(f"yes {your_order} is here")
        try:
            how_many=int(input(f"how many {your_order} you want:"))
            if your_order=="rice":
                total=onekg_rice*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_order=="millets":
                total=onekg_millets*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_order=="grains":
                total=onekg_grains*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            else:
                print("this item is not available")
                
    
           
        except:
            print("pls type correct name")
            
def stationary_products():
    one_pencil=25
    one_pen=30
    one_note=40
    items=["pencil","pen","note"]
    your_order=input("which item is you want:")
    if your_order in items:
        print(f"yes {your_order} is here")
        try:
            how_many=int(input(f"how many {your_order} you want:"))
            if your_order=="pencil":
                total=one_pencil*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_order=="pen":
                total=one_pen*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            else:
                print("this item is not available")
        except:
            print("pls type crt item name")
            
def food_court():
    one_sandwich=30
    one_pizza=100
    one_burger=85
    foods=["sandwich","pizza","burger"]
    your_order=input("which food is you want:")
    if your_order in foods:
        print(f"your {your_order} is ready")
        try:
            how_many=int(input(f"how many {your_order} you want:"))
            if your_order=="sandwich":
                total=one_sandwich*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_order=="pizza":
                total=one_pizza*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_order=="burger":
                total=one_burger*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
                
            else:
                print("this item is not available")
        except:
            print("pls type crt item name")
def dresses():
    one_chudi=1200
    one_leggins=550
    womens_section=["chudi","leggins"]
    your_choice=input("which type of dresses you want:")
    if your_choice in womens_section:
        print(f"yes {your_choice} is available")
    var=input("do you want to purchase womens section? press yes:")
    if var=="yes":
        print("pls go to right side of womens section!!!")
    else:
        print("thanks for visiting...")
        try:
            how_many=int(input(f"how many {your_choice}'s you want:"))
            if your_choice=="chudi":
                total=one_chudi*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_choice=="leggins":
                total=one_leggins*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            else:
                print("this dress is not available")
        except:
            print("pls type crt dress name")
def cheppals():
    one_slipper=200
    one_heels=500
    varieties=["slipper","heels"]
    your_choice=input("which cheppal is you want:")
    if your_choice in varieties:
        print(f"your {your_choice} is available!!!")
        try:
            how_many=int(input(f"how many {your_choice} is you waant:"))
            if your_choice=="slipper":
                total=one_slipper*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            elif your_choice=="heels":
                total=one_heels*how_many
                print(f"your total bill is {total}")
                f=open("bill.txt","w")
                f.write(f"your total bill is {total}")
                print("bill generated sucessfully")
                x=datetime.datetime.now()
                print(f"your bill is generated on {x}")
            else:
                print("sorry this cheppal is not available")
        except:
            print("pls enter crt name ")
                
    
        
                
        
    
                
                
            