###
### LIN 537 Fall 2021
### HW7
### arpabet.py
### NAME: WRITE YOUR NAME HERE

import nltk.corpus

def get_transcrdict():
    """This function reads in NLTK's cmudict corpus
    and returns a dictionary mapping words to their transcriptions,
    where transcriptions are lists of ARPABET phones
    inputs:
        none
    returns:
        dict (str:list(str)): dictionary mapping word strings
                         to their ARPABET transcriptions"""
    transcrdict = {}
    #The instructor completed this function in 5 lines
    ### YOUR CODE HERE
    return transcrdict

def get_phonedict(transcrdict):
    """This function takes a dictionary mapping words to ARPABET 
    phone lists and returns a dictionary mapping phones to sets of
    words that contain those phones. It removes stress annotation
    from the phones
    inputs:
        transcrdict dict(str:list(str): dict mapping words to phone lists
    returns:
        dict (str:set(str)) dict mapping phones to the set of words that contains that phone"""
    phonedict = {}
    # The instructor completed this function in 6 lines
    ### YOUR CODE HERE
    return phonedict

def words_by_phone(phonedict):
    """This function prompts the user to input a phone and a number,
    it prints the first n words (alphabetically) that contain that phone. 
    The function will end when the user inputs the empty string as the phone
    inputs:
        phonedict dict(str:set(str)): dict mapping phones to sets of words
    returns:
        None"""
    # The instructor solved this in 12 lines
    ### YOUR CODE HERE
    return

def phones_by_word(transcrdict):
    """This function prompts the user to input a word. It outputs the ARPABET transcription. The function ends if the user inputs the empty string. If the user inputs an unknown word, it asks them to try again
    inputs:
        transcrdict dict(str:list(str)): dict mapping words to list of phones
    returns:
        None"""
    # The instructor solved this in 7 lines
    ### YOUR CODE HERE
    return

def main():
    transcrdict = get_transcrdict()
    phonedict = get_phonedict(transcrdict)
    while True:
        print("What do you want to do?")
        print("1: display a word's transcription")
        print("2: print words that contain a phone")
        print("3: exit")
        selection = input("? ")
        if selection == "1":
            phones_by_word(transcrdict)
        elif selection == "2":
            words_by_phone(phonedict)
        elif selection == "3":
            exit()
        else:
            print("Your selection was not recognized. Try again.")
    

if __name__=="__main__":
    main()
