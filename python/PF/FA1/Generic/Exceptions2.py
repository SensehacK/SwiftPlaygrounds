'''
Created on Feb 16, 2017

@author: kautilya.save
'''

class Excelp (Exception):
    def __init__(self):
        message = "Excelp is the exception"
        
        super().__init__(message)   



def func(a,b):
    try :
        if a == "R" :
            raise Excelp()
        
    except ValueError :
        print("V")
    except TypeError:
        print("TE")
#     except Excelp  as sae:
#         print("AYarl", sae)
#     except :
#         print("aseaeASfa")
    finally:
        print("IF")

try :
    func("R",13)
    print("Hello")
except ValueError :
    print("V")
except Exception as e:
    print("AS" , e)
finally : 
    print("OF")
