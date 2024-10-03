import os
import re

# Get only the files in the pull request
changed_files = os.getenv('CHANGED_FILES').split() 

def validate_test_class_name(changed_files):
    errors = []

    # Filter only metadata files
    apex_files = [file for file in changed_files if file.endswith(".cls")]

    if apex_files:
        apex_classes = []
        for class_Use in apex_files:
            with open(class_Use, 'r', encoding='utf-8') as f:
                fullClass = f.read()
                if re.search("public class ", fullClass):
                    endTrimClass = fullClass.split("public class ")
                elif re.search("private class ", fullClass):
                    endTrimClass = fullClass.split("private class ")
                classSeparate = endTrimClass[1].split(" {", 1)
                apex_classes.append(classSeparate[0])
        for className in apex_classes:
            if re.search("(Test)$", className) == None:
                testEquivalent = className + "Test"
                numOfTest = apex_classes.count(testEquivalent)
                if numOfTest == 0:
                    errors.append(f"The class {className} does not have a test class")

    # Return success or failure based on errors found
    if errors:
        print(f"Errors: {errors}")
        raise ValueError("At least one class does not have a matching test class")
    else:
        print("All classes have matching test classes.")
        return 0  # Return 0 if all fields pass validation

validate_test_class_name(changed_files)