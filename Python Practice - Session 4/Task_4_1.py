"""Read names from file, sort the names and write them
   to a new file called sorted_names.txt
"""

with open('data/unsorted_names.txt') as input_file,\
     open('sorted_names.txt', 'w') as output_file:
    data = input_file.read().split()
    output_file.write('\n'.join(sorted(data)))
