''' Import standard library packages. '''
import py_compile
import platform
import os
import sys

'''
    Compilation of the solution to .pyc files, the compiled solution will be available
    in the compilation folder.
'''

if platform.system().lower() == 'linux':
    clear = lambda :os.system('clear')
    mkdir_comp = lambda :os.system('mkdir Compilation')
    mkdir_lib = lambda :os.system('mkdir Compilation/library')
    mkdir_input = lambda :os.system('mkdir Compilation/input_files')
    copy_file = lambda :os.system('cp input_files/test.txt Compilation/input_files/test.txt')
else:
    clear = lambda :os.system('cls')
    mkdir_comp = lambda :os.system('mkdir Compilation')
    mkdir_lib = lambda :os.system('mkdir Compilation\library')
    mkdir_input = lambda :os.system('mkdir Compilation\input_files')
    copy_file = lambda :os.system('copy input_files\\test.txt Compilation\input_files\\test.txt')

def main():
    clear()
    print("\nCompilation Started.")
    mkdir_comp()
    mkdir_lib()
    mkdir_input()
    copy_file()

    py_compile.compile('main.py', cfile = 'Compilation/main.pyc')
    py_compile.compile('library/__init__.py', cfile = 'Compilation/library/__init__.pyc')
    py_compile.compile('library/employee_manager.py', cfile = 'Compilation/library/employee_manager.pyc')
    py_compile.compile('library/file_manager.py', cfile = 'Compilation/library/file_manager.pyc')
    py_compile.compile('library/output_manager.py', cfile = 'Compilation/library/output_manager.pyc')

    print('Compilation Finished.')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Compilation EXCEPT: ', str(e))
        sys.exit(99)
    print()
