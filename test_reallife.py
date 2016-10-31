import unittest
from real_life import Employee
class EmlpoyeeClassTest(unittest.TestCase):
	def test_employee_instance(self):
		mfanyikazi = Employee()
		self.assertIsInstance(mfanyikazi, Employee, msg='The object should be an instance of the `Employee` class')
	def test_employee_name(self):
		mfanyikazi = Employee("Mandela")
		
		self.assertEqual(mfanyikazi.name,"Mandela", msg ="")
    def test_












if __name__ == '__main__':
    unittest.main()
