class Employee:
    def __init__(self,employee_id,employee_name,employee_age):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_age = employee_age
    def work(self):
        print(self.employee_id)
        print(self.employee_name)
        print(self.employee_age)
class manager(Employee):
    def arrange(self):
        print("arrange")
emp=manager(employee_id=101,employee_name="irfan",employee_age=34)
emp.work()
emp.arrange()