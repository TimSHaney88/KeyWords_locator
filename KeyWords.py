
#count how many occurances of keywords in file

def main():

    keyWords = {"and", "as", "assert", "break", "class", 
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}
    
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r") # Open the file
    print("Words from file and occurances: ")
    wordCounts = {} # Create an empty dictionary to count words
    for line in infile:
        print(line)
        processLine(line.lower(), wordCounts)
    
     
    pairs = list(wordCounts.items()) # Get pairs from the dictionary   
    
    #print(pairs)
    print()
    items = [[count, word] for (word, count) in pairs] 
    items.sort(reverse = True) # Sort pairs in items
    print("KeyWords: ", keyWords)
    print()
    print("Occurances of KeyWords")
    
    
    for count, word in items[0 : 100]: # Slice the first 10 items
        if word in keyWords:
            print(word, count, sep =  '\t')


    
        
    

# Count each word in the line
def processLine(line, wordCounts): 
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split() # Get words from each line
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1 # Add an item in the dictionary

# Replace punctuation in the line with space
def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line

main() # Call the main function

