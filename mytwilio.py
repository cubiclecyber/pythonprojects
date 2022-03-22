number = (input("Enter a number: "))

if number%2 == 0 and number%4 !=0:
    print("Even")
    if number%4 ==0:
        print("Divisible by four")
    elif number%8 ==0:
        print("Divisible by 8")
else:
    print("Odd")

Write a program that displays all prime numbers between 1 and 6,000.
Hint: A prime number is a number that is divisible by ONLY 1 and itself.

nums = list(range(0,20))

for number in range(0,20):
    for num2 in range(2, number):
        if number%num2 == 0:
            break
    else:
        print(number)
rows = input("enter number of rows :")
for row in range(int(rows)):
    print("*"*int(row))


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

while True:
    vacation = input("If would visit one place, where would it be?")
    if vacation =="end":
        break
    else:
        vacation = input("If would visit one place, where would it be?")

       





       
    
