import os
import sys

def sentence_splitter(file_name):
    f = open(os.path.join(sys.path[0], file_name), "r", encoding='utf-8') #opens the file from the currect directory

    #strips newline character if there are any and puts each seperate word into an array
    one_long_string = ""
    for line in f:
        one_long_string += line.replace('\n', " ")
    string_array = one_long_string.split()
    f.close()

    sentences = []
    sentence_end_index = -1 
    sentence_boundary = [".", "?", "!"]
    titles = ["Mr","Mrs","Dr","Jr"]

    f = open(os.path.join(sys.path[0], file_name), "w", encoding='utf-8') #opens the file from the currect directory

    for i in range(0, len(string_array)):
        if string_array[i][-1] in sentence_boundary: #checks if the last character of a word is a sentence boundary
            if string_array[i][:-1] not in titles: #If it is, then check if the word is a title
                try:
                    if string_array[i+1][0].isupper(): #checks if the first letter of the next word is a capital letter
                        f.write(" ".join(string_array[sentence_end_index+1:i+1])+"\n")
                        sentences.append(" ".join(string_array[sentence_end_index+1:i+1]))
                        sentence_end_index = i
                except:
                    f.write(" ".join(string_array[sentence_end_index+1:])+"\n")
                    sentences.append(" ".join(string_array[sentence_end_index+1:]))
    f.close()


sentence_splitter("test_short_text.txt")