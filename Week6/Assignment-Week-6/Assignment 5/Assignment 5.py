import os
import sys

def hapax(file_name):
    f = open(os.path.join(sys.path[0], file_name), "r", encoding='utf-8') #opens the file from the currect directory, and since the .txt is encoded in utf-8, that is specified as an argument
    word_count = {} #dictionary to store the amount of times every word is mentioned
    hapax_words = [] #list to store hapax words
    for line in f:
        string = line #reads the line and puts it inside variable stirng
        string = string[:-1] #gets rid of the newline character
        string = string.translate({ord(i): None for i in '.,!?:;()@/$"'}) #removes unecessary symbols
        string = string.lower() #sets every word into lower capital
        for x in string.split(" "): #splits the string into a list of strings
            if x not in word_count:
                word_count[x] = 1
            else:
                word_count[x] += 1
    f.close()
    for word in word_count:
        if word_count[word] == 1:
            hapax_words.append(word)
    return hapax_words

print(hapax("metamorphosis.txt"))
