import re

def convert(mystr):  
    wordList = re.sub("[',']", " ",  mystr).split()
    return wordList