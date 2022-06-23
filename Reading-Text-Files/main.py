# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, 'r') as read_file:
        file = read_file.read()
    
    return file


def count_words():
    text = read_file_content("./story.txt")
    
    sym = "!@#$%^&*()<>,./?:;"
    clean_word = [
        x.strip(x[-1]) if x[-1] in sym else x for x in text.split()
    ]
    
    dict_ = {}
    for x in clean_word:
        if x not in dict_.keys():
            dict_[x] = clean_word.count(x)

    return dict_
