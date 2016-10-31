class Employee(object):
    """ Base class for the differnt types of employees"""
    total_employees = 0
    def __init__(self,name=None,salary=None ):
      """ Initialising employee class"""
      self.name  = name
      self.salary = salary
      bEmployee.total_employees +=1
    
    def _get_total(self):
      """Returns total number of employees"""
      return Employee.total_employees
    
    total =property(_get_total)
   
    def _set_name(self,n):
      """ Sets Employee name"""
      self._name = n

    def _get_name(self):
      """Returns employee name"""
      return self._name
    name = property(_get_name,_set_name)
    def _set_salary(self,n):
   	    self._salary = s
    def _get_salary(self):
      """ Returns Employee Salary"""
      return self._salary
    salary = property(_get_salary,_set_salary)

class PartTime(object):
  """class for part time working times"""
  def __init__(self):
		self.minimum_weektime = "20 hrs"
		self.minimum_totaltime = "90 days"

    

class FullTime(object):
  """class for full time working times"""
  def __init__(self):
		self.minimum_weektime = "40 hrs"
		self.minimum_totaltime="indefinite"


class Lecturer(Employee,FullTime):
  """ Class for lectures"""
  def __init__(self,faculty, name, salary):
    """ Initializing lecturer class"""
    self.faculty =faculty
    self.name = name
    self.salary = salary


class NonTeachingStaff(Employee):
  """ Class for non teaching personnel"""
  def __init__(self,department,name, salary):
        self.department =department
        super(NonTeachingStaff, self).__init__(name, salary)

class AssistantLec(Lecturer,PartTime):
  """ Class for non assistant lectures"""
  def __init__(self,faculty,name, salary):
        self.faculty =faculty
        self.name = name
        self.salary = salary

