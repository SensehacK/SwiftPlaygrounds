'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from classes import FoodModule
from utility import DBConnectivity
from functionality import ViewFunctionsBilling
#from functionality.Registration import is_registered_user

def checkout(username):
    print("*********************************************")
    print("         Welcome to CheckOut !!! ")
    print("*********************************************")
    
    print("Items added successfully to the Cart !!!")
    print("Checkout in progress")
    print()
    
    print("Items Ordered")
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t  \t " ,value)
        
    print()
    print("Please Select from the below menu ")
    print()
    checkout_final(username)


def checkout_final(username):
    checkout_choice = input("Do you wish to proceed for billing or cancellation of any item or Save for later ? (Y/C/S) " )
    
    print("Your Selected Choice is : ")
    print(checkout_choice)
    print()
    
    if checkout_choice.upper() == 'Y': 
        #print("Hello checkout_choice == 'Y'")
        checkout_Yes(username)

    elif checkout_choice.upper() == 'C' :
        #print("Hello checkout_choice == 'C'")
        checkout_Cancel(username)
    
    elif checkout_choice.upper() == 'S' :
        #print("Hello checkout_choice == 'S'")
        checkout_Save(username)
    else :
        print("Please enter from the given choices only (Y,C,S). Thank you.")
        checkout_final(username)

def checkout_Yes(username):
    #print("Checkout Yes")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t \t " ,value)
    is_registered_user_flag = FoodModule.Food.is_registered_user
    
    if is_registered_user_flag == False :
        print("Guest User Logging in")
        FoodModule.Food.registered_user = 'Guest'
    
    
    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        '''
        SQL statement which is to be executed using bind variables
        #insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);
        '''
        is_cart_saved = FoodModule.Food.is_cart_saved
        print(username)
        print("is_cart_saved")
        print(is_cart_saved)
        if is_cart_saved :
            print("In  if is_cart_saved  ")
            
            cur.execute("delete from checkoutcart where username =:user_n",{"user_n": username})
            
            FoodModule.Food.is_cart_saved = False

        if FoodModule.Food.is_cart_saved == False :
            print("In  if is_cart_saved  == False ")
            for index , value in FoodModule.Food.cart_dict.items() :
                cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})
            
            #Saving the flag for Direct Module 4 execution that The cart is been saved once for this registered user
            FoodModule.Food.is_cart_saved = True
    
    
    
    
    
    
    
    
    
    
    
#     try:
#         con=DBConnectivity.create_connection()
#         cur=DBConnectivity.create_cursor(con)
#         username = FoodModule.Food.registered_user
#         '''
#         Example Query to be executed by using bind variables
#         #insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);
#         '''
#         
#         for index , value in FoodModule.Food.cart_dict.items() :
#             cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})
#             
    finally :
        '''
        Remove the print statement
        '''
        print("Closing the cursor & connections in def checkout_Yes(username):")
        
        FoodModule.Food.cart_dict.clear()
        cur.close()
        con.commit()
        con.close()
    
    '''
    #Call Module 4 Billing
    '''
    ViewFunctionsBilling.start_billing()
    
def checkout_Cancel(username):
    #print("checkout_Cancel")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  \t" ,value)
    
    food_name=input("Please select item for cancellation :")
    username = FoodModule.Food.registered_user
    
    #Deleting selected item from Dictionary
    itempop = FoodModule.Food.cart_dict.pop(food_name)
    print("Item popped :" , itempop)
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  \t" ,value)
    
    #Calling Functions
    checkout_final(username)

def checkout_Save(username):
    #print("checkout_Save")
    print("Saving to Database Checkout Cart")
    is_cart_saved = FoodModule.Food.is_cart_saved
    print("first _username")
    print(username)
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t " ,value)
        
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        '''
        SQL statement which is to be executed using bind variables
        #insert into checkoutcart (username ,foodname , quantity) values ('Kautilya','Masala', 200);
        '''
        print(username)
        print("is_cart_saved")
        print(is_cart_saved)
        if is_cart_saved :
            print("In  if is_cart_saved  ")
            
            cur.execute("delete from checkoutcart where username =:user_n",{"user_n": username})
            
            FoodModule.Food.is_cart_saved = False

        if FoodModule.Food.is_cart_saved == False :
            print("In  if is_cart_saved  == False ")
            for index , value in FoodModule.Food.cart_dict.items() :
                cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})
            
            #Saving the flag for Direct Module 4 execution that The cart is been saved once for this registered user
            FoodModule.Food.is_cart_saved = True
        
    finally :
        #print("Closing the cursor & connections in def checkout_Yes(username):")
        print("Item Saved Successfully!!!")
        FoodModule.Food.cart_dict.clear()
        cur.close()
        con.commit()
        con.close()
        

#print("Item Saved Successfully!!!")
    
