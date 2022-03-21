# Prompt the user to input the marks.
# The input should be between 0 and 100. 
# Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


# grade1 = input("Enter the marks :")
# grade = int(grade1)
# if grade >=79 and grade<=100:
#     print("A")
# elif grade >=60 and grade <79:
#     print("B")
# elif grade >=49 and grade <=59:
#     print("C")
# elif grade >=40 and grade <49:
#     print("D")
# elif grade <40:
#     print("E")
# else:
#     print("Incorrect marks")

# Write a program that has an array or a list(only in python)  a = [5, 10, 15, 20, 25]. 
# Make a new array/list of only the first and last elements of the given array/list above


a = [5, 10, 15, 20, 25]
print (a)
b = [a[0], a[-1]]
print(b)

# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
#If the number is a multiple of 4, display out a different message


noinput = input("Enter the number :")
noinput1 = int(noinput)
if (noinput1 %2 ) == 0 and (noinput1 %4) !=0 :
    print("Number is even")
elif (noinput1 %4) == 0 :
    print("Multiple of 4")
else:
    print("Number is odd")


# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”


phone = list(input("Enter your phone number :"))
if phone[0] == "0" and phone[1] == "7" and len(phone)==10:
    del phone[0]
    phone.insert(0, "+"), phone.insert(1, "2"),phone.insert(2, "5"), phone.insert(3,"4")
    formatted1 = ''.join(phone)
    print(formatted1)
elif phone[0] == "0" and phone[1] =="1" and len(phone)==10 :
    del phone[0]
    phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")
    formatted2 = ''.join(phone)
    print(formatted2)
elif phone[0] == "7" and len(phone)==9:
    phone.insert(0, "+"), phone.insert(1, "2"), phone.insert(2, "5"), phone.insert(3, "4")
    formatted3 =''.join(phone)
    print(formatted3)
elif phone[0] == "2" and phone[1] =="5" and phone[2] == "4" and len(phone)==12:
    phone.insert(0,"+")
    formatted4 = "".join(phone)
    print(formatted4)
elif phone[0] == "+" and phone[1] == "2" and phone[2] == "5" and phone[3] =="4" and len(phone) ==13:
    formatted5 ="".join(phone)
    print(formatted5)

else:
    print("Number is not correct")

# Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@” )


# email = input("Enter your email adress : ")
# if "@" in email  and "." in email and len(email) >=7 :
#     print("Correct email adress")
# elif "." in email  and len(email) >=7 :
#     print("email must contain a '@' ")
# elif "@" in email  and len(email) >=7 :
#     print("Email adress must have a'.'")
# elif  "@" in email  and "." in email :
#     print("Email entered is  too short")
# else:
#     print("Is that even an email adress?")


# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 


a = int(input("First number :"))
b = int(input("Second number :"))
c = int(input("Third number :"))

if  c<a>b :
    print(a)
elif c<b>a :
    print(b)
elif a<c>b :
    print(c)