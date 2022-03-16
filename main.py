# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

def incept(**k):
	env_rcvars="env PYTHONPATH="
	python,script=sys.executable,sys.argv
	PYPATHORG=os.environ.get('PYTHONPATH')
	PYPATHPYX=os.path.dirname(os.path.dirname(python))
	PYPATHSCR=os.path.dirname(script[0])
	PYPATHPKG=os.path.dirname(os.path.dirname(script[0]))
	PYTHONPATH='{}:{}:{}:{}'.format(PYPATHPYX,PYPATHSCR,PYPATHPKG,)
	os.environ['PYTHONPATH']=PYTHONPATH
	env=os.environ
	args = [helper, python] + script # + [os.environ]
	os.execvpe(helper, args, os.environ)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
