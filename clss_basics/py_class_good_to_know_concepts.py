
class Employee:
    """This variable to is common to all Internal Employee object"""
    org_name = "abc"
    def __init__(self,empid, name):
        self.empid = empid
        self.name = name

    """With @classmethod the method can be accessed Class.methodname() ie without creating object"""
    @classmethod
    def get_org_name(cls):
        print(cls.org_name)


class InternalEmployee(Employee):
    """This variable to is common to all Internal Employee object.
    Also private for this class.We use _varname to make a variable private.
    anyways u can access this outside class, by using mangling"""
    _standard_salary = 40000
    def __init__(self, empid,name):
        super().__init__(empid,name)  # super() will call parent class constructor here

    def process_salary(self):
        return self._standard_salary

    # Overriding this method will be used on printing our objects
    def __str__(self):
        return f'Employee id {self.empid} and name is {self.name}'

class HourlyEmployee(Employee):
    def __init__(self, empid, name):
        super().__init__(empid,name)  # super() will call parent class constructor here

    def process_salary(self,no_of_hrs):
        return self.__calculate_salary(no_of_hrs)

    """use __ to declare private method.A method can't be 
    accessed via object or class using . notation"""
    def __calculate_salary(self,no_of_hrs):
        return no_of_hrs * 1000;

def main():
    internal_employee = InternalEmployee("1","Mike")
    print(Employee.org_name)
    # internal_employee._standard_salary #AttributeError
    # print(Employee.empid) #AttributeError
    print(internal_employee.process_salary())
    Employee.get_org_name()
    """Below line will raise an AttributeError, 
    Since this method cant be accessed outside class..Lets use 
    Name Mangling to access private methods"""
    hrly_employee = HourlyEmployee("2","Peter")
    #print(hrly_employee.__calculate_salary(120))
    print(hrly_employee._HourlyEmployee__calculate_salary(120))
    """If u have overridden method __str__ in your class, with meaningful string 
    representation printing object will give u informative string"""
    print(internal_employee) #Employee id 1 and name is Mike
    """Printing object without overriding __str__"""
    print(hrly_employee) #<__main__.HourlyEmployee object at 0x00000122472783D0>



if __name__ == '__main__':
    main()
