class employee:
    def __init__(self, name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def increase_salary(self):
        self.salary= (self.salary*0.2)+self.salary
        return self.salary
    
    def print_salary(self):
        print(f"Increasing salary is {self.salary}")
    
emp1 = employee("Sarrok", 20,salary)
emp2 = employee("Saurav",19,salary )
emp1.increase_salary()
emp1.print_salary()

        
       
        
    
