# Function to modify content
def modify_content(content):
    # Example: Convert all text to uppercase
    return content.upper()

# Open the input file in read mode
with open("input.txt", "r") as input_file:
    # Read the content
    content = input_file.read()

# Modify the content
modified_content = modify_content(content)

# Open a new file in write mode to save the modified content
with open("output.txt", "w") as output_file:
    # Write the modified content to the new file
    output_file.write(modified_content)

print("File modified and saved successfully.")
