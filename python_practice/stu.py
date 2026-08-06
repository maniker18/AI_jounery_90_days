class emp:
    raise_pay = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def gmail(self):
        return f"{self.first}{self.last}@gmail.com"

    @gmail.setter
    def gmail(self, new_email):
        # Split the new email at @
        # new_email = "man.ker@gmail.com"
        parts = new_email.split("@")  # ["man.ker", "gmail.com"]
        username = parts[0]  # "man.ker"
        
        # Split username at . to get first and last
        name_parts = username.split(".")  # ["man", "ker"]
        
        # Update first and last
        self.first = name_parts[0]  # "man"
        self.last = name_parts[1]   # "ker"
        
        # Note: The domain part is ignored
    



    def full_name(self):
        return f"full name is :{self.first} {self.last}"

    @full_name.deleter
    def full_name(self):
        print("deleted")
        self.full_name="unwa"


    def hike(self):
        self.pay = self.pay * self.raise_pay
        return self.pay

    @classmethod
    def str(cls, str):
        first, last, pay = str.split("-")
        return cls(first, last, pay)

     



    def __repr__(self):
        return f"emp ({self.first} , {self.last} , {self.pay})"

    def __str__(self):
        return f"emp ({self.full_name()} , {self.pay}, {self.hike()})"

# Test the code
emp_1 = emp("mani", "ker", 100)

print("=== Initial values ===")
print(emp_1.gmail)    # maniker@gmail.com
print(emp_1.first)    # mani

print("\n=== Changing email ===")
emp_1.gmail = "man.ker@gmail.com"

print("\n=== After change ===")
print(emp_1.first)    # man (changed from mani)
print(emp_1.last)     # ker
print(emp_1.gmail)    # manker@gmail.com (NOT man.ker@gmail.com!)

del emp_1.full_name

class dev(emp):
    def __init__(self, first, last, pay,course):
        super().__init__(first, last, pay)
        self.course = course


class man(emp):
    def __init__(self, first, last, pay,no_of_emp= None):
        super().__init__(first, last, pay)
        if no_of_emp == None:
           self.no_of_emp=[]
        else:
            self.no_of_emp=no_of_emp

    def add_emp(self,emp):
        if emp  not in self.no_of_emp:
            self.no_of_emp.append(emp)

    def remove_emp(self,emp):
        if emp   in self.no_of_emp:
            self.no_of_emp.remove(emp)

    def print_all(self):
        for emp  in self.no_of_emp:
            print(emp.full_name())

    def no_of(self):
        
        print(len(self.no_of_emp))


    

# emp_1=emp("mani","ker",100,)
# emp_2=emp("ram","kam",100,)
# emp_3=emp("jam","nam",100,)
# emp_4=emp("sam","tam",100,)

# print(emp_1)

# manage_1 =man("jay","shetty",100,[emp_1,emp_2])
# manage_1.print_all()
# manage_1.no_of()










# emp=emp("ram","kam",100,)
# emp_str2.raise_pay = 1.05
# print(f"{emp_str2.full_name()} and  cousre is :  {emp_str2.hike()}")
# print(f"{emp_str1.full_name()} and  cousre is : {emp_str1.hike()}")
# print(emp1.hike())
# print(emp1.no_of_emp)
# print(emp2.hike())
# print(emp2.no_of_emp)

