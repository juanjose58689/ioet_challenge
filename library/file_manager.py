''' Import standard library packages. '''
import re
import os

class File_Manager():
    '''
        This class contain methods to manage the file or files, validate them and extrac the 
        required information according to the required standard input format.

        This class has two classmethods:
            - extract_schedule: This method verifies if the path is a single file and validate if the file exists and is a ".txt"
                                file; or if the path a folder that contains various files, in wich case it extract all the ".txt" 
                                files and read the information from them and return a dictionary.
            - extract_employee_info: This method is used to extract the information of each employee and format it in a "Day, Start,
                                     End" form in order to use this in the salary calculation.
        
        And has four staticmethods:
            - validate_extension: This method validates if the file passed is a ".txt", if not it raises an exception.
            - validate_exist: This method validates if the file passed exists.
            - extract_files: This method extracts all the ".txt" files in the folder passed.
            - drop_blank_lines: This methods drops the blank lines in the file passed

        This class raise exceptions in various scenarious:
            - Repeated employee name whitin a file or amogn the various files.
            - No employee information in any file.
            - The information is not formatted correctly and does not have the "=" sign.
            - The information is not formatted correctly in the worked time (DayStart-End).
            - The file passed with the -d/--document is not a ".txt" file.
            - The file passed with the -d/--document does not exist.
            - The folder passed with the -f/--folder does not have any ".txt" file.
    '''
    
    @classmethod
    def extract_schedule(cls, path):
        employees = {}
        if os.path.isdir(path):
            files = cls.extract_files(path)
            for file in files:
                employees_aux = cls.extract_employee_info(os.path.join(path, file))
                for name in employees_aux.keys():
                    if name in employees.keys():
                        raise Exception(f"Error, repeated employee name '{name}' in file: '{file}'")
                employees.update(employees_aux)
        else:
            cls.validate_extension(path)
            cls.validate_exist(path)
            employees = cls.extract_employee_info(path)

        if not employees:
            raise Exception("No employees we're found in files(s)")
        return employees

    @classmethod
    def extract_employee_info(cls, file):
        with open(file = file, mode = 'r') as f:
            employee_dic = {}
            for line in cls.drop_blank_lines(f):
                day_array = []
                try:
                    (name, all_schedules) = line.split('=')
                except:
                    raise Exception(' Error in the input file "=" sign.')
                else:
                    if name in employee_dic.keys():
                        raise Exception(f"Error, repeated employee name in file: '{file}'")

                    for x in all_schedules.split(","):
                        try:
                            day_schedule = re.match(r'(?P<Day>[A-Za-z]+)(?P<Start>\d+:\d+)-(?P<End>\d+:\d+)', x)
                            group_day = day_schedule.groupdict()
                            day_array.append(group_day)
                        except:
                            raise Exception("Invalid input format: Day, Start or End")

                    employee_dic[name] = day_array

        return employee_dic

    @staticmethod
    def validate_extension(filename):
        extension = os.path.splitext(filename)[-1].lower()
        if extension != '.txt':
            raise Exception(f' File {filename} is not a ".txt" file.')

    @staticmethod
    def validate_exist(filename):
        if not os.path.exists(filename):
            raise Exception(f' File {filename} does not exist.')

    @staticmethod
    def extract_files(path):
        files = []
        for name in os.listdir(path):
            files.append(name if os.path.splitext(name)[-1].lower() == '.txt' else None)
        if not files:
            raise Exception(' There are not ".txt" files in the provided folder.')
        return files

    @staticmethod
    def drop_blank_lines(file):
        for lin in file:
            line = lin.rstrip()
            if line:
                yield line