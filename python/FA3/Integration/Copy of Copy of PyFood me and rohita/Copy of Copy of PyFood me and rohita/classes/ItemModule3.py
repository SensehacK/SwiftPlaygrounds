'''
Created on Mar 15, 2017

@author: kautilya.save
'''


'''
This class represents a product
'''

class ItemCategories:
    def __init__(self):
        self.__fcid=None
        self.__categoryName=None
        self.__restaurant_Type=None


    def get_fcid(self):
        return self.__fcid


    def get_category_name(self):
        return self.__categoryName


    def get_restaurant_type(self):
        return self.__restaurant_Type


    def set_fcid(self, value):
        self.__fcid = value


    def set_category_name(self, value):
        self.__categoryName = value


    def set_restaurant_type(self, value):
        self.__restaurant_Type = value



class CategoryItems:
    def __init__(self):
        self.__ciid=None
        self.__foodName=None
        self.__price=None
        self.__availability=None
        self.__restaurantFK=None
        self.__categoryFK=None

    def get_ciid(self):
        return self.__ciid


    def get_food_name(self):
        return self.__foodName


    def get_price(self):
        return self.__price


    def get_availability(self):
        return self.__availability


    def get_restaurant_fk(self):
        return self.__restaurantFK


    def get_category_fk(self):
        return self.__categoryFK


    def set_ciid(self, value):
        self.__ciid = value


    def set_food_name(self, value):
        self.__foodName = value


    def set_price(self, value):
        self.__price = value


    def set_availability(self, value):
        self.__availability = value


    def set_restaurant_fk(self, value):
        self.__restaurantFK = value


    def set_category_fk(self, value):
        self.__categoryFK = value
        
        