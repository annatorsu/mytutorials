class Employee:
    def __init__(self, first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name+"."+last_name+"@company.com"
    def fullname(self):
        return "{}{}".format(self.first_name,self.last_name)

empl_1=Employee("Anna","Torsu",6000)
empl_2=Employee("Test","user",7000)

print(empl_1.email)
print(empl_2.email)

print(empl_1.fullname())
print(Employee.fullname(empl_1))
