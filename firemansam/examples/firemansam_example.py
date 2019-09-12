from firemansam.firedir import firedir
from firemansam.firecheck import firecheck
from firemansam.firedir import firedict
import os

# analyse example repository recursively
upgrade_list = firedir('example_repo')

# count number of Python files which do not conform to Python 3
upgrade_file_count = 0
file_count = 0
for file in upgrade_list:
    if file["scale"] > 0:
        upgrade_file_count += 1

# summarise results of analysis
print('\nNumber of Python files checked: ' + str(len(upgrade_list)))
print('\nNumber of Python files requiring upgrade to Python 3: ' + str(upgrade_file_count))
print('\nExample fix: ')
print('\n')

# present one example from analysis
filename = os.path.abspath(os.path.dirname(__file__)) + '/example_repo/examples/example_4.py'
print(firecheck(filename))
firedict(filename)
