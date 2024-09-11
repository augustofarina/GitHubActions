import os
import re
import sys

print('This is a python script running')
changed_files = os.getenv('CHANGED_FILES').split()
print('os.getenv(CHANGED_FILES) ==> ')
print(os.getenv('CHANGED_FILES'))
print('Changed Files ==> ')
print(changed_files)
print(len(changed_files))