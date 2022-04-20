''' Import standard library testing package '''
import unittest
from datetime import datetime as dt
''' Import files and classes to be tested '''
from library.file_manager import File_Manager
from library.employee_manager import Employee_Manager
from library.output_manager import Output_Manager

file = 'unit_testing/unit_test_file.txt'
folder = 'unit_testing/test_folder'
output = 'unit_testing/output_test.txt'

class Test_FileManager_Methods(unittest.TestCase):
    ''' Class to test the File_Manager methods. '''
    def test_extract_employee_info(self):
        self.assertEqual(File_Manager().extract_employee_info(file) , {'RENE': [
                                {'Day': 'MO', 'Start': '10:00', 'End': '12:00'}, 
                                {'Day': 'TU', 'Start': '10:00', 'End': '12:00'}, 
                                {'Day': 'TH', 'Start': '01:00', 'End': '03:00'}, 
                                {'Day': 'SA', 'Start': '14:00', 'End': '18:00'}, 
                                {'Day': 'SU', 'Start': '20:00', 'End': '21:00'}], 
                            'ASTRID': [
                                {'Day': 'MO', 'Start': '10:00', 'End': '12:00'}, 
                                {'Day': 'TH', 'Start': '12:00', 'End': '14:00'}, 
                                {'Day': 'SU', 'Start': '20:00', 'End': '21:00'}]})
    
    def test_extract_files(self):
        self.assertEqual(File_Manager().extract_files(folder), ['tfile_1.txt', 'tfile_2.txt', 'tfile_3.txt'])

class Test_EmployeeManager_Methods(unittest.TestCase):
    ''' Class to test the Employee_Manager methods. '''
    employee_info = Employee_Manager('RENE', [  {'Day': 'MO', 'Start': '10:00', 'End': '12:00'}, 
                                                {'Day': 'TU', 'Start': '10:00', 'End': '12:00'}, 
                                                {'Day': 'TH', 'Start': '01:00', 'End': '03:00'}, 
                                                {'Day': 'SA', 'Start': '14:00', 'End': '18:00'}, 
                                                {'Day': 'SU', 'Start': '20:00', 'End': '21:00'}])
    def test_calculate_salary(self):
        self.assertEqual(self.employee_info.salary, 215)
        
    def test_validate_hours(self):
        format_ = "%H:%M"
        start = dt.strptime("10:00", format_)
        end = dt.strptime("18:00", format_)
        self.assertTrue(self.employee_info.validate_hours(start, end, 'MO'))

class Test_OutputManager_Methods(unittest.TestCase):
    ''' Class to test the Output_Manager methods. '''
    employee_info = Employee_Manager('RENE', [ {'Day': 'MO', 'Start': '10:00', 'End': '12:00'}, 
                                                                {'Day': 'TU', 'Start': '10:00', 'End': '12:00'}, 
                                                                {'Day': 'TH', 'Start': '01:00', 'End': '03:00'}, 
                                                                {'Day': 'SA', 'Start': '14:00', 'End': '18:00'}, 
                                                                {'Day': 'SU', 'Start': '20:00', 'End': '21:00'}])
    def test_validate_exist(self):
        self.assertFalse(Output_Manager(output, self.employee_info).validate_exist(output))
    
    def test_validate_extension(self):
        self.assertTrue(hasattr(Output_Manager(output, self.employee_info).validate_extension(), '__self__'))

if __name__ == '__main__':
    print('\nTesting Started.')
    unittest.main()