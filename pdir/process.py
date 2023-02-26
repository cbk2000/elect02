import os

INPUT_DIR = '../input'
OUTPUT_DIR = '../output'

# Set input and output file paths
INPUT_FILE = os.path.join(OUTPUT_DIR, 'DUMMY-REGISTRATION.csv')
INPUT_FILE_CLEAN = os.path.join(OUTPUT_DIR, 'DUMMY_REGISTRATION.csv')
os.rename(INPUT_FILE, INPUT_FILE_CLEAN)

OUTPUT_FILE_NAME = 'OS_GH_USERNAME.txt'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, OUTPUT_FILE_NAME)

# Check if output file exists and delete it if specified by user
if os.path.isfile(OUTPUT_FILE):

    # Delete output file if it already exists
    os.remove(OUTPUT_FILE)

# Write data from input file to output file
with open(INPUT_FILE_CLEAN, 'r') as input_file, open(OUTPUT_FILE, 'w') as output_file:
    for line in input_file:
        columns = line.strip().split(',')
        output_file.write(columns[4] + '\n')

# Delete first line of output file
with open(OUTPUT_FILE, 'r+') as f:
    f.readline()
    data = f.read()
    f.seek(0)
    f.write(data)
    f.truncate()

exit(0)
