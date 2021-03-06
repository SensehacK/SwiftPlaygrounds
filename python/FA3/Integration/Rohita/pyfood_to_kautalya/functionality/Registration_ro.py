'''
Created on Mar 16, 2017

@author: venkata.goparaju
'''
from functionality import Restaurants
from database import ViewDB
from functionality import Login
from classes import RegistrationModule
from validations import All_validations
is_registered_user = False

def correct_password(username):
    input2 = input("Enter the password:")
    if All_validations.validate_existing_password(username,input2):
        input3 = input("Confirm password:")
        if input2 == input3:
            if All_validations.validate_password(input2) == True:
                ViewDB.update_password(username,input2)
                print("your password is resetted")
                return True
            else:
                print("Your password does not meet the requirements, please refill them")
                return False
        else:
            print("Please check the password and type again")
            return False
    else:
        register()

def new_registration(name):
#     name = input("Enter the username:")
#     if Login.check_username(name) == True:
    print("your registration is in process")
    customer = RegistrationModule.Customer()
    customer.set_username(name)
    email_id = input("Enter the emailid:")
    if All_validations.validate_email(email_id):
        customer.set_emailid(email_id)
    else:
        register()
    mobile_number = input("Enter the mobile number:")
    if All_validations.validate_phone_number(mobile_number):
        customer.set_mobilenumber(mobile_number)
    else:
        register()
#             password = input("Enter the password:")
    flag = False
    while flag == False:
        pass_word1 = input("Enter the password:")
#         if All_validations.validate_existing_password(name,pass_word1):
        pass_word2 = input("Confirm the password:")
        if pass_word1 == pass_word2:
            if All_validations.validate_password(pass_word1) == True:
                customer.set_password(pass_word1)
                flag = True
                break
            else:
                print("your password did not match the crieteria")
        else:
            print("your passwords did not match. please reenter them")
#         else:
#             register()
    question = input("Enter the secret question:")
    customer.set_question(question)
    answer = input("Enter your answer:")
    customer.set_answer(answer)
    cityname = input("Enter your city:")
    customer.set_city(cityname)
    area = input("Enter your area:")
    customer.set_area(area)
    state = input("Enter your state:")
    customer.set_state(state)
    ViewDB.insert_new_user(name,email_id,mobile_number,pass_word1,question,answer,cityname,area,state)
    print("Registration successfull")
    
    username1 = input("Enter the username:")
    password1 = input("Enter the password:")
#     if All_validations.validate_existing_password(name,pass_word1):
    if ViewDB.login(username1,password1):
        city = ViewDB.login(username1,password1).get_city()
        area = ViewDB.login(username1,password1).get_area()
        print(city)
        print(area)
        Restaurants.restaurants()
#     else:
#         register()
#     else:
#         print("Username already exists!!!")
#         input("Enter new username:")
def register():
    print("Enter your choice:")
    print("a. Guest user:")
    print("b. Login")
    print("c. New Registration")
    
    choice = input("Enter your choice:")
    
    if choice == 'a':
        print("You are not eligible for discounts")
        city = input("Enter your city name:")
        area = input("Enter your area name:")
        Restaurants.restaurants()
    
    if choice == 'b':
        global is_registered_user
        is_registered_user = True
#         try:
        username = input("Enter the username:")
        if Login.check_username(username) == True:
            print("First do the registration")
            register()
#             list_of_username=ViewDB.validate_username(username)
            
#         except:
#             pass
        if All_validations.validate(username) != False:
            password = input("Enter the password:")
#             if All_validations.validate_existing_password(username,password):
            if ViewDB.login(username,password):
                city = ViewDB.login(username,password).get_city()
                area = ViewDB.login(username,password).get_area()
                print(city)
                print(area)
                Restaurants.restaurants()
            else:
                input1 = input("Reenter password or Forgot password? (R/F)")
                if input1 == 'R':
                    print("Reenter password")
                    i=0
                    while(i<3):
                        username = input("Enter the username:")
                        password = input("Enter the password:")
                        if All_validations.validate_password(password) == True:
                            print("please wait while you are redirected")
                            city = ViewDB.login(username,password).get_city()
                            area = ViewDB.login(username,password).get_area()
                            print(city)
                            print(area)
                            Restaurants.restaurants()
                        i += 1
                    print("You have exceeded the number of attempts, please try resetting your password")
                    register()
                elif input1 == 'F':
                    flag = False
                    print("Forgot password")
                    question = ViewDB.check_question(username).get_question()
                    print(question[0])
                    answer = input("Enter the answer:")
                    ans = ViewDB.check_answer(username).get_answer()
                    print(answer)
                    print(ans)
                    output_ans = ans[0]
                    print(output_ans)
                    if answer == output_ans:
                        print("your answer is right")
                        if ViewDB.security_question(username, answer):
                            print("inside the security question")
                            flag = True
                        else:
                            flag = False
                    if flag == False:
                        print("your answer is wrong")
                        register()
                          
                    if flag == True:
                        if correct_password(username) == True:
                            pass
                    if correct_password(username) == False:
                        correct_password(username)
#             else:
#                 register()
        else:
            register()
#                         flag = 0
#                         print("Please check the password and type again")
#                         flag = 1
#                         correct_password(username)
#                         if flag == 0:
#                             print("Your password does not meet the requirements, please refill them")
                        
                    
                        
    if choice == 'c':
        name = input("Enter the username:")
        if All_validations.validate(name) != False:
            if Login.check_username(name) == True:
                new_registration(name)
            else:
                print("Username already exists!!!")
                name = input("Reenter the username:")
                if Login.check_username(name) == True:
                    new_registration(name)
        else:
            register()
            
    else:
        print("Please give your input as a, b, or c only")
        register()
