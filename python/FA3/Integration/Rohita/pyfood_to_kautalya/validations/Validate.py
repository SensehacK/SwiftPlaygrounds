'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from database import ViewDB
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException , Validate_item_present , Validate_item_available


def validate_view_category(restaurant_type): 
#     print("///////////////////validate_view_category////////////////////")
#     print("In validate function class  /validate_view_category")
#     print("In validate function class  /validate_view_category")
    
    list_of_restaurant_categories=ViewDB.get_restaurant_categories(restaurant_type)
    if(len(list_of_restaurant_categories)==0):
        #print("Raising Exception")
        raise InvalidCategoryException()
    
    return list_of_restaurant_categories


def validate_view_category_items(category,restaurant):
#     print("///////////////////validate_view_category_items////////////////////")
#     print("In function validate_view_category_items") 
    
    list_of_restaurant_categories_items=ViewDB.get_categories_fooditems(restaurant,category)
    if(len(list_of_restaurant_categories_items)==0):
        #return False
        raise InvalidCatItemsException
    return list_of_restaurant_categories_items

def validate_item_present(category_items):
#     print("///////////////////validate_item_present////////////////////")
#     print("In function validate_item_present")
#     print("In validate function class  /validate_item_present")
   
    list_of_restaurant_categories=ViewDB.get_selected_food_items_present(category_items)
    if(len(list_of_restaurant_categories)==0):
        #print("Raising Exception")
        raise Validate_item_present()

    return list_of_restaurant_categories


def validate_item_available(restaurant_type):
#     print("///////////////////validate_item_available////////////////////")
#     print("In function validate_item_available")
#     print("In validate function class  /Validate_item_available")
    
    list_of_item_available=ViewDB.get_food_items_availability(restaurant_type)
    if 'NA' in list_of_item_available :
        #print("Raising Exception")
        #return False
        raise Validate_item_available()
      
    else :
        #print("All Available validate function class  /Validate_item_available")
        return True
        

def validate_input_is_decimal(input_number):
    try : 
            if (int(input_number)) :
                #print("Valid Decimal Input")
                return True
    except Exception :
            print("Please enter a Decimal Number!")
            return False
    


