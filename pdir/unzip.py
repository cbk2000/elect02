import os
import zipfile


input_dir = os.path.join('../', 'input')
output_dir = os.path.join('../', 'output')

# Check if input directory exists
if not os.path.isdir(input_dir):
    print(f"Error: {input_dir} directory does not exist.")
    exit(1)

# Set input file path
input_file = os.path.join(input_dir, 'DUMMY-REGISTRATION.csv.zip')

# Check if output directory exists and create it if it doesn't
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# Unzip input file to output directory
with zipfile.ZipFile(input_file, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

exit(0)
