#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest = lambda x,y,z : (x*y*z)/100

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    #print("Platinum Member�)
    print("Platinum member")
else :
    print("Gold Member")
    #print(�Gold Member�)
