''' Import standard library packages. '''
import os
import csv

class Output_Manager():
    '''
        This class is designed to implement a writer for the output files. It validates if the file already exist
        and ask for override permition. This class implement various output file types, currently is it supports
        ".txt" and ".csv" files and could implement another extension in an easy way. This class validates if the 
        desired output extension is supported and raise an exception if not.

        To implement a new output file type a function to write should be implemented, and add the extension and
        function to the supported_extensions dictionary in the validate_extension method. The information of the
        employees is a list of Employee_Manager objects and has the ".name" and ".salary" attributes.
    '''

    def __init__(cls, filename, employee_info):
        cls.filename = filename
        cls.employee_info = employee_info
        cls.extension = os.path.splitext(filename)[-1].lower()
        
    def write_output(cls):
        writer = cls.validate_extension()
        if cls.validate_exist(cls.filename):
            override = str(input(f'File {cls.filename} already exists. Do you want to override it? [y/Y][n/N]: ')).lower()
            if override == 'n':
                raise Exception(f'File {cls.filename} already exists and override was denied. Try another name for the output file.')

        writer()
        
    def validate_extension(cls):
        supported_extensions = {'.txt': cls.write_txt, '.csv': cls.write_csv}
        if cls.extension not in supported_extensions.keys():
            raise Exception(f' Extension {cls.extension} is not currently supported as output.')
        else:
            return supported_extensions[cls.extension]

    def write_txt(cls):
        with open(cls.filename, mode = 'w') as f:
            for employee in cls.employee_info:
                f.write(f'The amount to pay {employee.name} is {employee.salary} USD\n')
        f.close()

    def write_csv(cls):
        with open(cls.filename, mode = 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Name', 'Salary'])
            for employee in cls.employee_info:
                csv_writer.writerow([employee.name, employee.salary])
        f.close()

    @staticmethod
    def validate_exist(filename):
        if not os.path.exists(filename):
            return False
        else:
            return True