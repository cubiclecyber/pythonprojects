# Class is a collection of related variables and functions.
# Inside a class a variable is called a property.
# Inside a class a function a method.
class Payroll():
    gs = 0
    nssf = 0
    ti = 0

    # Constructor is a method that runs automatically when object (variable belonging
    #  to the class) is created
    def __init__(self, ba=0, be=0):
        self.gs =  ba + be
        self.nssf_calculator()
        self.ti_calculator()

    def nssf_calculator(self):
        if self.gs < 18000:
            self.nssf = self.gs * 0.06
        else:
            self.nssf = 1080

    def ti_calculator(self):
        self.ti = self.gs - self.nssf

paul = Payroll(42000)
print(paul.gs)
print(paul.nssf)


class Vehicle():
    model=""
    make=""
    tyres = 0
    cc = 0
    passengers = 0

    def veh_type(self,model,make):
        self.model = model
        self.make = make
    
    def add_cc(self,cc):
        self.cc = cc

# Object is an instance of a class i.e it is a variable that comes from a certain class
v = Vehicle()
v.veh_type("Toyota","Vitz")
print(v.make)
print(v.cc)
v.add_cc(1300)
print(v.cc)

n = Vehicle()
n.veh_type("Nissan", "Juke")
n.add_cc(2000)
print(n.cc)