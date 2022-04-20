# Ioet, inc. Challenge

## Problem
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:
| Day                 | Start | End   | Salary |
|---------------------|-------|-------|--------|
| Monday to Friday    | 00:01 | 09:00 | 25 USD |
| Monday to Friday    | 09:01 | 18:00 | 15 USD |
| Monday to Friday    | 18:01 | 00:00 | 20 USD |
| Saturday and Sunday | 00:01 | 09:00 | 30 USD |
| Saturday and Sunday | 09:01 | 18:00 | 20 USD |
| Saturday and Sunday | 18:01 | 00:00 | 25 USD |

Input:

	RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

Output:

	The amount to pay RENE is: 215 USD

The solution should provide a terminal aplication which has the goal to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked.

The input is a ".txt" file with rows as shown previously in "Input" and the result should be as the "Output" mentioned before, for each employee in the input file.

## How to run
Download this solution and open a terminal console in the downloaded location "ioet_challenge".

### Options
The program has various options (parameters), to see the list run the next command, it works in Windows and Linux.

`$ python3 main.py --help`

The options are as follows:
- -h, --help: Show the help message.
- -f FOLDER, --folder FOLDER: Path to folder that contains ".txt" file(s) to perfom the salary calculation.
- -d DOCUMENT, --document DOCUMENT: Path to ".txt" file to perform the salary calculation.
- -o OUTPUT, --output OUTPUT: Output file name where need to be saved the final information, accepts ".txt" and ".csv" files,
- --version: Outputs the program's version.
### Examples
- Run the code without parameters. The Input file will be input_files/test.txt.

	` $ python3 main.py `
- Run the code using the file "test_employees.txt". 

	` $ python3 main.py -d input_files/test_employees.txt`
- Run the code using all the ".txt" file in the input_files folder.

	` $ python3 main.py -f input_files`
- Run the code saving the results in the "output_files/output.txt" file.

	` $ python3 main.py -o output_files/output.txt`
## Compile
To compile the solution to a ".pyc" file, run the compile.py file as follows:

` $ python3 compile.py`

It will generate a folder called "Compilation" with the next structure:
- main.pyc
- library/
	- employee_manager.pyc
	- file_manager.pyc
	- output_manager.pyc
- input_files/
	- test.txt

## Test
For the unit testing of the solution were implemented six unit-test, each for one method of any class described in the next section.

To perfom the test run the next command:

`$ python3 unit_test.py -v`

## How it works
In order to approach this problem, an object-oriented solution was implemented. Three classes were implemented to manage the different sides of the challenge.

### File_Manager class
To read the file(s) and extract the input information needed, the claas File_Manager in file_manager.py was implemented. This class implements static methods to validate the extension and the existance of the file and raise exception if the input file does not exist or is not a ".txt" file.

```python
@staticmethod
def validate_extension(filename):
	extension = os.path.splitext(filename)[-1].lower()
	if extension != '.txt':
		raise Exception(f' File {filename} is not a ".txt" file.')

@staticmethod
def validate_exist(filename):
	if not os.path.exists(filename):
		raise Exception(f' File {filename} does not exist.')
```

In the case that a folder were passed to the solution as input, the class has an static method to search the ".txt" files in the provided folder path.

```python
@staticmethod
def extract_files(path):
	files = []
	for name in os.listdir(path):
		files.append(name if os.path.splitext(name)[-1].lower() == '.txt' else None)
	if not files:
		raise Exception(' There are not ".txt" files in the provided folder.')
	return files
```

Finally the purpose of this class is shown when te employee worked time information is extracted and formatted using the regular expression python package.

```python
for x in all_schedules.split(","):
	try:
		day_schedule = re.match(r'(?P<Day>[A-Za-z]+)(?P<Start>\d+:\d+)-(?P<End>\d+:\d+)', x)
		group_day = day_schedule.groupdict()
		day_array.append(group_day)
	except:
		raise Exception("Invalid input format: Day, Start or End")
```

### Employee_Manager class

This class calculates the salary to be payed to the employee based on the days and hours worked, for this, the class has some constant values that represents the wages on each turn , the days, the start and the end of the 09:00 - 18:00 turn. This class is implemented in employee_manager.py file.

```python
days = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}
wages = [25 / 3600, 15 / 3600, 20 / 3600, 30 / 3600, 20 / 3600, 25 / 3600]
start_turn = dt(year = 1900, month = 1, day = 1, hour = 9, minute = 0)
end_turn = dt(year = 1900, month = 1, day = 1, hour = 18, minute = 0)
```

Then the calculate_salary method computes the amount to be payed according to the next factors:

- Day: Based on the day of the week, the wages are selected from the constat "wages". So for week-days (Monday to Friday) wages 1, 2 and 3 are selected: for weekend (Saturday and Sunday) wages 4, 5, 6 are selected.

```python
if cls.days[day['Day']] < 5:
	wage_1, wage_2, wage_3 = cls.wages[:3]
else:
	wage_1, wage_2, wage_3 = cls.wages[3:]
```

### Output_Manager

This class, implemented in output_manager.py, is used to save the salary calculation results in an specified file.

It implements methods to validate existance of the file and provides a selection to even override the file or stop the program and use a different name.

```python
def write_output(cls):
	...
	if cls.validate_exist(cls.filename):
		override = str(input(f'File {cls.filename} already exists. Do you want to override it? [y/Y][n/N]: ')).lower()
		if override == 'n':
			raise Exception(f'File {cls.filename} already exists and override was denied. Try another name for the output file.')

@staticmethod
def validate_exist(filename):
	if not os.path.exists(filename):
		return False
	else:
		return True
```

It also has the possibility to writte different extensions files, such as ".txt" and ".csv" files, implementig a validate_extension method.

```python
def validate_extension(cls):
	supported_extensions = {'.txt': cls.write_txt, '.csv': cls.write_csv}
	if cls.extension not in supported_extensions.keys():
		raise Exception(f' Extension {cls.extension} is not currently supported as output.')
	else:
		return supported_extensions[cls.extension]
```

And a function for each extension.

- TXT
	```python
	def write_txt(cls):
		with open(cls.filename, mode = 'w') as f:
			for employee in cls.employee_info:
				f.write(f'The amount to pay {employee.name} is {employee.salary} USD\n')
		f.close()
	```

- CSV
	```python
	def write_csv(cls):
		with open(cls.filename, mode = 'w') as f:
			csv_writer = csv.writer(f)
			csv_writer.writerow(['Name', 'Salary'])
			for employee in cls.employee_info:
				csv_writer.writerow([employee.name, employee.salary])
		f.close()
	```




