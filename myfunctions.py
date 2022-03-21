
def gross_salary(a,b):
    x = a + b
    return x

def nhif(gross_salary):
    if gross_salary <6000:
        nh = 150
    elif gross_salary > 6000 and gross_salary<7999:
        nh =    300
    elif 8000>gross_salary<11999:
        nh =400
    elif 12000 >gross_salary< 14999:
        nh=500
    elif 15000 >gross_salary< 19999:
        nh=600
    elif 20000 >gross_salary< 24999:
        nh=750
    elif 25000 >gross_salary< 29999:
        nh=850
    elif 30000 >gross_salary< 34999:
        nh=900
    elif 35000 >gross_salary< 39999:
        nh=950
    elif 40000 >gross_salary< 44999:
        nh=1100
    elif 50000 >gross_salary< 59999:
        nh=1200
    elif 60000 >gross_salary< 69999:
        nh=1300
    elif 70000 >gross_salary< 79999:
        nh=1400
    elif 80000 >gross_salary< 89999:
        nh=1500
    elif 90000 >gross_salary< 99999:
        nh=1600
    else:
        nh= 1700
    return (nh)

def nssf(g):
    if g < 18000:
        nssf = g * 0.06
    else:
        nssf = 1080
    return nssf

def payee(t):
    if ti <= 24000:
        payee = 0.1 * ti
    elif (ti - 24000) <= 8330:
        payee = 2400 + ((ti - 24000) * 0.25)
    else:
        payee = 2400 + 2082.5 + ((ti - 32330) * 0.3)
    return payee

h = int(input("Enter basic salary: "))
i = int(input("Enter benefits: "))

f = gross_salary(int(h),int(i))
print("Gross: ",f)

nhif = nhif(f)
print("NHIF: ", nhif)

nssf = nssf(f)
print("NSSF: ", nssf)

ti = f - nssf
print("Taxable Income: ",ti)

payee = payee(ti)
print("PAYEE: ", payee)

netsalary = f - nhif - nssf - payee + 2400
print("Net Salary: ",netsalary)


#taxrelief  =  2400
