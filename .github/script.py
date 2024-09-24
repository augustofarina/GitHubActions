import os
import re

# Get only the files in the pull request
changed_files = os.getenv('CHANGED_FILES').split() 

def validate_field_descriptions(changed_files):
    errors = []

    # Regular expression to match <description></description>
    #description_regex = re.compile(r'<description>(.*?)<\/description>', re.DOTALL)
    #description_tag = "<description>"
    description_regex = re.compile(r'<description>\s*([\S\s]*?)\s*<\/description>', re.DOTALL)
    className_regex = re.compile(r'public class [A-Z][a-z]+(?:[A-Z][a-z]+)*(Handler|Helper|Controller)$')

    # Filter only metadata files
    object_files = [file for file in changed_files if file.endswith("__c.field-meta.xml")]
    apex_files = [file for file in changed_files if file.endswith(".cls")]

    if apex_files:
        for object_Use in apex_files:
            with open(object_path, 'r', encoding='utf-8') as f:
                contentClass = f.read()
                classes = className_regex.findall(contentClass)
                if not classes:
                    raise ValueError("The class name isn't matching the established naming conventions")

    if not object_files:
        return 0  # No custom object files to validate

    # Validate each file
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
    if errors:
        print(f"Errors: {errors}")
        raise ValueError("At least one custom field does not has a description")
    else:
        print("All custom fields have valid descriptions.")
        return 0  # Return 0 if all fields pass validation

validate_field_descriptions(changed_files)