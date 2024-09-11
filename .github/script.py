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

def validate_field_descriptions(changed_files):
    """Check if custom fields in metadata files from pull request have a description with at least one letter."""
    errors = []

    # Regular expression to match <description>...</description>
    description_regex = re.compile(r'<description>(.*?)<\/description>', re.DOTALL)

    # Filter only metadata files
    object_files = [file for file in changed_files if file.endswith(".object-meta.xml")]

    if not object_files:
        print("No custom field metadata files changed.")
        return 0  # No custom object files to validate

    # Validate each file
    for object_path in object_files:
        # Open and read the file content
        with open(object_path, 'r', encoding='utf-8') as f:
            content = f.read()

            # Find all description tags
            descriptions = description_regex.findall(content)

            # Check each description
            for description in descriptions:
                if not description.strip() or not re.search(r'[a-zA-Z]', description):
                    errors.append(f"File {object_path} contains a field with an invalid description.")

    # Return success or failure based on errors found
    if errors:
        for error in errors:
            print(error)
        #return 1  # Return 1 if any errors are found
    else:
        print("All custom fields have valid descriptions.")
        #return 0  # Return 0 if all fields pass validation