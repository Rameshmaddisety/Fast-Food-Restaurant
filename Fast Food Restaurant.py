def orderMethod(cust_ZipCode,orderOption,fB):
    print("Menu")
    print("Dear Customer Please your Menu \n(a) Flyers Burger: $4.50 per an order \n(b) Flyers Drink: $1.50 per a container\n(c) Flyers Fries: $ 2.50 per an order\n(d) Flyers Dessert: $ 3.00 per an order")
    option =str(input())
    bill=fB
    if option=='a':
        bill=bill+4.50
    elif option=='b':
        bill=bill+1.50
    elif option=='c':
        bill=bill+2.50
    elif option=='d':
        bill=bill+3.50
    else:
        print("Please Select Correct Order")
        print("-----Thank You-----")
    final_Bill=bill+((5/100)*bill)
    if orderOption== "Delivery" or orderOption== "delivery":
        if cust_ZipCode==60446:
            final_Bill=final_Bill+5
        elif cust_ZipCode==60451 or cust_ZipCode==60441:
            final_Bill=final_Bill+7
    
    print("You want to order Something type, Yes")
    reorder =str(input())
    if reorder == 'Yes' or reorder == 'yes':
        print("Sure please select Your items")
        final_Bill=orderMethod(cust_ZipCode,orderOption,bill)
    return final_Bill
    

print("----------Dear Customer Welcome To Fast Food Restaurant----------\n")

print("Dear Customer Please select/enter your options 'Pick-Up' or 'Delivery'\n")

orderOption= str(input())

print("Dear Customer Enter your Zip-Code for Deliver Your Order...\n")

cust_ZipCode = int(input())

final_Bill=0
if cust_ZipCode==60446:
    print("Dear Customer Delivery is Available for your Area\n")
    final_Bill=orderMethod(cust_ZipCode,orderOption,final_Bill)
elif cust_ZipCode==60451 or cust_ZipCode==60441:
    print("Dear Customer Delivery is Available with extra cost for your Area\n")
    final_Bill=orderMethod(cust_ZipCode,orderOption,final_Bill)
else:
    print("Dear we Apologise Delivery Not Available for your Area\n")

if orderOption== "Pick-Up":
    print("Dear Customer Your order is Ready please Pick up from the Restaurant")
    print("Your Bill is  $:",final_Bill)
    print("----------Thanks for The Order, Have a good day----------\n")
else:
    
    print("Dear Customer Your order is on the way please wait for sometime...")
    print("Your Bill is  $:",final_Bill)
    print("----------Thanks for The Order, Have a good day----------\n")
