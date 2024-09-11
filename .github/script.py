import os
import re
import sys

print('This is a python script running')
changed_files = os.getenv('CHANGED_FILES').splitlines()
print('Changed Files ==> ' + changed_files)