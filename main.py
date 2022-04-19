'''
	Import argparse and get the options:
		-f, --folder: Folder path to work with and extract ".txt" files.
		-d, --document: Document path to work with.
		-o, --output: Output file name/path to save the results.

		--version: Program's version.
'''
import argparse

parser = argparse.ArgumentParser( prog = 'IOET CHALLENGE',description="Calculates salary for the hours worked based on the day of the week and time of the day.")
parser.add_argument( '-f', '--folder', nargs = 1, metavar = 'FOLDER', type = str, required = False, help =' Folder from wich extrarct the ".txt" files with employess schedules.')
parser.add_argument( '-d', '--document', nargs = 1, metavar = 'DOCUMENT', type = str, default = ['input_files/test.txt'], help =' Document with employess schedules.')
parser.add_argument( '-o', '--output', nargs = 1, metavar = 'OUTPUT', type = str, required = False, help =' Name of output document if intended to be saved, if not provided only console print will be shown.')
parser.add_argument( '--version', action = 'version', version = '%(prog)s 1.0')

p_opts = parser.parse_args()

''' Import standard library packages '''
import os
import sys
import platform

''' Import custom packages '''
from library.file_manager import File_Manager
from library.employee_manager import Employee_Manager
from library.output_manager import Output_Manager

''' Creation of lambda function to clear the terminal screen based on the OS '''
if platform.system().lower() == 'linux':
	clear = lambda :os.system('clear')
else:
	clear = lambda :os.system('cls')

def main():
	'''
		Main function performs the cleaning of the terminarl screen, creates the object for the different manager classes
		and executes the needed methods.

		For the extract_schedule method, the path priority depends of the -f/--folder parameter, if -f/--folder parameter
		is passed to the code it will be used instead of the -d/--document parameter.

		If the -o/--output parameter is passed, the results will be saved in the spicified file,
		currently the class Output_Manager supports ".txt" and ".csv" files.
	'''
	clear()
	print('\nProgram started')

	manager = File_Manager()
	employees_schedule = manager.extract_schedule(path = p_opts.folder[0] if p_opts.folder else p_opts.document[0])
	employees_salary = [Employee_Manager(name, schedule) for (name, schedule) in employees_schedule.items()]

	for employee in employees_salary:
		print(f'The amount to pay {employee.name} is: {employee.salary} USD')
	
	if p_opts.output:
		output = Output_Manager(p_opts.output[0], employees_salary)
		output.write_output()

	print('Program Finished.')

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("Main EXCEPT:", str(e))
		sys.exit(99)
	print()