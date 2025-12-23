
class EmployeeSalary:
    salary = 0

    def __init__(self,name,hours,rest_days,email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.hourly_payment = 400 ## Если имелось ввиду именно это решение, то просьба подсказать где про такое почитать, в тренажере не помню такого, чтобы тут были значения которых нет в строке __init__

    @classmethod
    def get_hours(cls,name, hours, rest_days, email):
        if hours == None:
            hours = (7 - rest_days) * 8
            return cls(name, hours, rest_days, email)

    @classmethod    
    def get_email(cls,name, hours, rest_days, email):
        if email == None:
            email = f"{name}@email.com"
            return cls(name, hours, rest_days, email)
        
    @classmethod
    def set_hourly_payment(cls, x):
        cls.hourly_payment = x
        
    def salary(self):   
        salary = self.hours * self.hourly_payment
        return salary



### Для проверки вызова функций 

###get_hours
#employeeSalary = EmployeeSalary.get_hours('Evgen', None ,2 , 'mail@mail.ru')
#print(employeeSalary.__dict__)

###get_hours
#employeeSalary = EmployeeSalary.get_hours('Evgen', None ,2 , 'mail@mail.ru')
#print(employeeSalary.__dict__)

###set_hourly_payment
#EmployeeSalary.set_hourly_payment(4)
#print(EmployeeSalary.hourly_payment)

###salary
##employeeSalary = EmployeeSalary('Evgen', 12 ,2 , 'mail@mail.ru')
##print(employeeSalary.salary())






