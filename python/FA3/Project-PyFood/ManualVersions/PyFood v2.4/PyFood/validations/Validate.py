'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from database import ViewDB,searchdb
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException , Validate_item_present , Validate_item_available
from exceptions import CustomException2
from classes import FoodModule

def validate_view_category(restaurant_type): 
#     print("///////////////////validate_view_category////////////////////")
#     print("In validate function class  /validate_view_category")
#     print("In validate function class  /validate_view_category")
    
    list_of_restaurant_categories=ViewDB.get_restaurant_categories(restaurant_type)
    if(len(list_of_restaurant_categories)==0):
        #print("Raising Exception")
        FoodModule.Food.restaurant_name = None
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

def validate_item_present(category_items,restaurant_name):
#     print("///////////////////validate_item_present////////////////////")
#     print("In function validate_item_present")
#     print("In validate function class  /validate_item_present")
    
    list_of_restaurant_categories=ViewDB.get_selected_food_items_present(category_items,restaurant_name)
    if(len(list_of_restaurant_categories)==0):
        #print("Raising Exception")
        raise Validate_item_present()

    return list_of_restaurant_categories


def validate_item_available(category_items,restaurant_name):
#     print("///////////////////validate_item_available////////////////////")
#     print("In function validate_item_available")
#     print("In validate function class  /Validate_item_available")
#     print("len(category_items)")
#     print(len(category_items))
        
    list_of_item_available=ViewDB.get_food_items_availability(category_items,restaurant_name)
#     print("list_of_item_available")
#     print(list_of_item_available)
    
    if(len(list_of_item_available)==0):
        print("No Rows Returned for that selected items")
        return False
    
    else : 
        #If different number of rows returned compared to input & then not valid availability
        if len(category_items) != len(list_of_item_available) :
            return False
        
        elif 'NA' in list_of_item_available :
            #print("Raising Exception")
            raise Validate_item_available()
            #return False
        
        else :
            #print("All Available validate function class  /Validate_item_available")
            return True
        

def validate_input_is_decimal(input_number):
    try : 
        if (int(input_number)) == 0 :
            return True
        elif (int(input_number)) :
            #print("Valid Decimal Input")
            return True
    except Exception :
            print("Please enter a Decimal Number!")
            return False




''' 
Gaurav Validations

'''


def validate_search_category(city,area): 
    list_of_search_categories=searchdb.search_as_a_guest(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidcityareaname()
    
        
    return list_of_search_categories
   
def validate_search_as_rating(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_likes(city,area): 
    list_of_search_categories=searchdb.search_as_likes(city,area)
    if(len(list_of_search_categories)==0):
        print("noooooooo")
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
    
    
def validate_search_as_dislikes(city,area): 
    list_of_search_categories=searchdb.search_as_dislikes(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislikes(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_dislikes(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_likes(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_likes(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_type(city,area,rating_lower,rating_upper,var): 
    list_of_search_categories=searchdb.search_as_rating_type(city,area,rating_lower,rating_upper,var)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_like(city,area): 
    list_of_search_categories=searchdb.search_as_dislike_like(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_dislike_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_like_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_like_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislike_like(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_dislike_like(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislike_type(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_rating_dislike_type(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_like_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_dislike_like_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_like_type_rating(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_like_type_rating(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_all(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_all(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories

def validate_hotel_name(city,area,restaurant_name): 
    list_of_search_categories=searchdb.hotel_name(city,area,restaurant_name)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories


def validate_highest_rated(): 
    list_of_search_categories=searchdb.search_highest_rated()
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories

