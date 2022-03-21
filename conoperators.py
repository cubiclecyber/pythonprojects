#CONDITIONAL OPERATORS:
    #or- if 1 condition is true, the whole is true
    #and- if 1 condition is false, the whole condition is false
#1.take user email adress,
#check if the email adress is valid
#2.ask user for phone no
#check if its valid, i.e, phone >=9 and less than 14




from distutils.util import convert_path


email = input("Enter your email adress : ")
#conv = ("@") and (".") and (len >6) in email
conv = "@" in email and "." in email and len(email) >=9
print(conv)

phone_no = input("Enter your phone number : ")
phonec=len(phone_no) >=9 and len(phone_no)<=14
print(phonec)

