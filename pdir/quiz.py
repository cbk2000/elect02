#!/usr/bin/env python3

import os

pdir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join('../', 'input')
input_file = 'input.txt'
input_path = os.path.join(input_dir, input_file)
output_dir = os.path.join('../', 'output')
output_file = 'output.txt'
output_path = os.path.join(output_dir, output_file)


if not os.path.isdir(input_dir):
    print("Error: input directory does not exist.")
    exit(1)

if not os.path.isfile(input_path):
    print("Error: input file does not exist.")
    exit(1)

if not os.path.isdir(output_dir):

    # create the output directory if it doesn't exist
    os.makedirs(output_dir)

if os.path.isfile(output_path):

    # remove the output file if it already exists
    os.remove(output_path)


section_header = ""
question_contents = ""
answer = ""

last_line = sum(1 for line in open(input_path))
current_line = 0


with open(input_path, 'r') as f:
    for line in f:
        current_line += 1

        if line.startswith('ZCZC'):
            section_header = line

        if line.startswith('T:'):
            question_contents = line[2:].strip()
            answer = 'A'
        elif line.startswith('F:'):
            question_contents = line[2:].strip()
            answer = 'B'

        if line.strip() and not line.startswith(('T:', 'F:')):
            question_contents += '\n' + line.strip()

        if (not line.strip() or current_line == last_line) and answer in ('A', 'B'):
            with open(output_path, 'a') as out_file:
                out_file.write("# ############# XXXXX\n")
                out_file.write(section_header)
                out_file.write(question_contents + "\n")
                out_file.write("---\n")
                out_file.write("A. true\n")
                out_file.write("B. false\n")
                out_file.write("ANSWER: {}\n".format(answer))
                out_file.write("\n")

            question_contents = ""
            answer = ""

exit(0)