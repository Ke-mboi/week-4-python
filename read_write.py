# File Read & Write Challenge

# Read from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (convert to uppercase as an example)
modified_content = content.upper()

# Write the modified content to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified version saved to 'output.txt'.")
