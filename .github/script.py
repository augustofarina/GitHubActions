import os
import re

# Get only the files in the pull request
changed_files = os.getenv('CHANGED_FILES').split() 

def validate_field_descriptions(changed_files):
    print("changed_files:")
    print(changed_files)
    errors = []

    # Regular expression to match <description></description>
    #description_regex = re.compile(r'<description>(.*?)<\/description>', re.DOTALL)
    #description_tag = "<description>"
    print("Running Regex")
    description_regex = re.compile(r'<description>\s*([\S\s]*?)\s*<\/description>', re.DOTALL)

    # Filter only metadata files
    object_files = [file for file in changed_files if file.endswith("__c.field-meta.xml")]

    print("First validation")
    if not object_files:
        print("No custom field metadata files changed.")
        return 0  # No custom object files to validate

    # Validate each file
    print("For validation")
    for object_path in object_files:
        # Open and read the file content
        with open(object_path, 'r', encoding='utf-8') as f:
            content = f.read()

            descriptions = description_regex.findall(content)

            if not descriptions:
                errors.append(f"File {object_path} is missing the <description> tag.")
            else:
                for description in descriptions:
                    # Check if the description contains any non-whitespace characters
                    if not description.strip():
                        errors.append(f"File {object_path} has an empty or whitespace-only <description> tag.")


            # Check each description
            #for description in descriptions:
                #if not description.strip() or not re.search(r'[a-zA-Z]', description):
                    #errors.append(f"File {object_path} contains a field with an invalid description.")

            #if description_tag not in content:
                #errors.append(f"File {object_path} is missing the <description> tag.")

    # Return success or failure based on errors found
    print("Error validation")
    if errors:
        for error in errors:
            print(error)
        return 2  # Return 1 if any errors are found
        print("Return?")
    else:
        print("All custom fields have valid descriptions.")
        return 0  # Return 0 if all fields pass validation

validate_field_descriptions(changed_files)