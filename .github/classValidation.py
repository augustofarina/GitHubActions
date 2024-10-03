import os
import re

# Get only the files in the pull request
changed_files = os.getenv('CHANGED_FILES').split() 

def validate_class_name(changed_files):
    errors = []

    className_regex = re.compile(r'(public|private) class [A-Z][a-z]+(?:[A-Z][a-z]+)*(Handler|Helper|Controller|Test)')

    # Filter only metadata files
    apex_files = [file for file in changed_files if file.endswith(".cls")]

    if apex_files:
        for object_Use in apex_files:
            with open(object_Use, 'r', encoding='utf-8') as f:
                contentClass = f.read()
                classes = className_regex.findall(contentClass)
                if not classes:
                    errors.append(f"The class {object_Use} isn't matching the established naming conventions")

    # Return success or failure based on errors found
    if errors:
        print(f"Errors: {errors}")
        raise ValueError("At least one class does not matches the naming conventions")
    else:
        print("All classes have matching fields have matching naming conventions.")
        return 0  # Return 0 if all fields pass validation

validate_class_name(changed_files)