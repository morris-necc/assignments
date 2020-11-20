import os
import sys

def average_word_length(file_name):
    f = open(os.path.join(sys.path[0], file_name), "r", encoding='utf-8') #opens the file from the currect directory
    total_length = 0
    total_words = 0
    for line in f:
        string = line #reads the line and puts it inside variable stirng
        string = string[:-1] #gets rid of the newline character
        string = string.translate({ord(i): None for i in '.,!?:;()@/$"'}) #removes unecessary symbols
        string = string.lower() #sets every word into lower capital
        for x in string.split(" "): #splits the string into a list of strings
            total_length += len(x)
            total_words += 1
    return total_length/total_words

print(average_word_length("the_brothers_karamazov.txt")) #test
