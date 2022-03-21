for j in range (1, 6001):
    count = 0
    for i in range(2, (j//2 + 1)):
        if(j % i == 0):
            count = count + 1
            break

    if (count == 0 and j != 1):
        print(" %d" %j, end = '  ')


# # Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# # A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

# marks = int(input("Input the marks to get the grade:"))
# if marks >=79 and marks<=100:
#     print("A")
# elif marks >=60 and marks <79:
#     print("B")
# elif marks >=49 and marks <=59:
#     print("C")
# elif marks >=40 and marks <49:
#     print("D")
# elif marks <40:
#     print("E")
# else:
#     print("Incorrect marks")

# # TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# # Write a program that takes the age in years and returns the age in days.Use 365 days as the length of a year for this challenge as we would like to ignore leap years. Only accept positive numbers.
# # Once you learn functions,re
dob = input("Enter your date of birth in format (DD/MM/YYYY) : ")
today = "19/03/2022"
tday = int(today[0:2])
tmonth =int(today[3:5])
tyear = int(today[6:])
day = int(dob[0:2])
month = int(dob[3:5])
year =int(dob[6:])
if month<=3 :
    yl = tyear - year
    ml = tmonth - month
    dl = tday- day
    status = "Your age is", yl, "Years,", ml,"Months,", dl,"days"
elif month>tmonth and day<=tday :
    yl = (tyear-1) - year
    ml = (tmonth+12) - month   
    dl =tday- day            
    status ="Your age is", yl, "Years,", ml,"Months,", dl,"days"
elif day >tday and month<=tmonth:
    yl = tyear - year
    ml = (tmonth-1) - month
    dl = (tday +30)- day
    status="Your age is", yl, "Years,", ml,"Months,", dl,"days"
elif day>tday and month>tmonth :
    yl = (tyear-1)- year
    ml = (tmonth+11) -month
    dl =(tday + 30)-day
    status="Your age is", yl, "Years,", ml,"Months,", dl,"days"
elif year>tyear:
    print("Incorrect date of birth")
else:
    print("Incorrect date ")





# # TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# # Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# # Once you learn fun 
# base = float(input("Enter the base of the triangle :"))
# height = float(input("Enter the height of the triangle :"))
# area = 1/2 * base * height
# print ("Area =",area)

# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print "Ok". Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# # For example, if the speed is 80, it should print: "Points: 2". If the driver gets more than 12 points, the function should print: "License suspended".
# speed = int(input("Enter the speed in Km/s :"))
# demerit = (speed-70)/5
# status=""
# if demerit<=0 :
#     status ="Okay"
# elif demerit <12 and demerit>0 :
#     status ="Points :", str(demerit)
# elif demerit>=12:
#     print("Your licence has been terminated!!")


# Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.
rows = int(input("How many rows do you want: "))
for i in range(rows):
    for j in range (i+1):
        print("*", end="")
    print()


# TASK 13: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

# prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
# total_stock = int( prods[0][2]) + int(prods[1][2]) + int(prods[2][2]) + int(prods[3][2])
# print(total_stock)

# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes 3 details (name,email and phone number) from a user as input, and stores them in one array/list then validates:
# i) if the email is valid
# ii) convert the phone to start from +254712345678 and
# iii) check if the name does not contain a number 
# If all these pass, print out the details in one list else display an error message.
# Once you learn functions,revisit this and write this code inside a function.

# name = input("Enter your name : ")
# if "1" in name or "2" in name or "3" in name or "4" in name or "5" in name or "6" in name or "7" in name or "8" in name or "9" in name  or "0" in name:
#     print("Oops..incorrect")
# else:
#     print("Looks good.")
# email = input("Good,now enter your email adress : ")
# if "@" in email  and "." in email and len(email)>=7:
#     print("Correct email adress, lets proceed")
# else:
#     print("Recheck your email adress")

# phone = list(input("Enter your phone number : "))
# status =""
# if phone[0] == "0" and phone[1] == "7" and len(phone)==10:
#     del phone[0]
#     phone.insert(0, "+"), phone.insert(1, "2"),phone.insert(2, "5"), phone.insert(3,"4")
#     status = ''.join(phone)
# elif phone[0] == "0" and phone[1] =="1" and len(phone)==10 :
#     del phone[0]
#     phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")
#     status = ''.join(phone)
# elif phone[0] == "7" and len(phone)==9:
#     phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")
#     status =''.join(phone)
# elif phone[0] == "2" and phone[1] =="5" and phone[2] == "4" and len(phone)==12:
#     phone.insert(0,"+")
#     status = "".join(phone)
# elif phone[0] == "+" and phone[1] == "2" and phone[2] == "5" and phone[3] =="4" and len(phone) ==13:
#     status ="".join(phone)
# print(name,"you entered the following details")
# print("Your name : ",name)
# print("Your email : " ,email)
# print("Phone number  : ",''.join(status))

# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user.
#  Assume that the user would not enter any two numbers which are the same

# first = int(input("Enter the first number : "))
# second = int(input("Enter the second number : "))
# third =int(input("Enter the third number : "))
# fourth = int(input("Enter the other number : "))

# if first>second and first>third and first>fourth :
#     print(first)
# elif second>first and second>third and second>fourth :
#     print(second)
# elif third>first and third>second and third>fourth :
#     print(third)
# elif fourth >first and fourth>second and fourth>third :
#     print(fourth)


# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then return user “Login is Successful” and ONLY accepts 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

count = 1

while count<4:
    email1 = input("Enter your email : ")
    password =("Enter your password : ")
    if  email1== "admin@mail.com" and password == "Admin@123" :
        print("Log in successful")
        break
    else:
        print("Login failed.. ")
        count +=1
  

# TASK 17: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.

# num_1 = input("Enter the first number :")
# num_2 = input("Enter second number : ")
# if num_1== int : 
#     sumint = int(num_1)+int(num_2)
#     print(sumint)
# elif type(sum)==float:
#     sumint = float(num_1)+float(num_2)
#     print(sumint)
# elif sum ==str:
#      print("Sting not accepted")


# TASK 18: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

# Once you learn functions,revisit this and write this code inside a function.

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using THIS LINK:  

# Once you learn functions,revisit this and write this code inside a function.

# TASK 20: Using Python or PHP or Java or Ruby or JavaScript
# To calculate the Employees Payee, you need to find the gross salary first then find the taxable income (this is the gross salary less the NHIF value) 

# i.e taxable_income = gross salary - NSSF

# Continue with the same program and find the person's PAYEE 
# quiz 18  # quiz 19  #quiz 20
# salary = float ( input ( 'Enter your Basic Salary: ' ) )
# benefits = float ( input ( 'Enter your Benefits: ' ) )
# gross_salary = (float ( salary ) + int ( benefits ))
# print ( float ( gross_salary ) )

# nhif = float ( 5 / 100 ) * gross_salary
# print ( "nhif :",float ( nhif ) )
# paye = float ( 10 / 100 ) * gross_salary
# print ( "payee:",float ( paye ) )
# nssf = float ( 6 / 100 ) * gross_salary  # 6% of gross salary
# print ("nssf", float ( nssf ) )

# taxable_income = gross_salary - nssf
# print ("taxaable-income :", float ( taxable_income ) )

# net_salary = gross_salary - (nhif + nssf + paye)
# print ( "Net salary :",net_salary)