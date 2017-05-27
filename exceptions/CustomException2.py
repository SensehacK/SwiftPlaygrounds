'''
Created on Mar 15, 2017

@author: kautilya.save
'''

'''
This file has all the custom exceptions needed for the project
'''

class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("The category is invalid")
        
        
class InvalidCatItemsException(Exception):
    def __init__(self):
        super().__init__("The category items is invalid")

class Validate_item_present(Exception):
    def __init__(self):
        super().__init__("The selected item is Not Available")

class Validate_item_available(Exception):
    def __init__(self):
        super().__init__("Selected item not Available!!! Please Select a different item")
