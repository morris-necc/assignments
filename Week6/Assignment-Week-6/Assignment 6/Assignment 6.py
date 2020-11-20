import os
import sys

def numbered_file(file_name):
    old_file = open(os.path.join(sys.path[0], file_name), "r", encoding='utf-8') #takes the file
    new_file = open(os.path.join(sys.path[0], "numbered_"+file_name), "w", encoding='utf-8') #makes a new file
    line_number = 1
    for line in old_file:
        line = str(line_number) + "     " + line #I put space here to make the numbers easier to read
        line_number += 1
        new_file.write(line)
    old_file.close()
    new_file.close()

numbered_file("divine_comedy.txt") #test