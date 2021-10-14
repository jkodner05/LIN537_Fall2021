###
### LIN 537 Fall 2021
### HW6
### count.py
### NAME: WRITE YOUR NAME HERE

def sortdict_byval(tokenfreqs, reverse):
    """This function sorts a dictionary by values
    and returns a list of (key, value) tuples
    inputs:
        tokenfreqs (dict (str, int)): dictionary to sort
        reverse (bool): whether to sort in ascending or descending(reversed) order
    returns:
        list of (str, int) tuples: in ascending or descending order"""
    ### This function is completed for you
    return sorted(tokenfreqs.items(), key=lambda kv: kv[1], reverse=reverse)

def update_count(sequence, tokenfreqs):
    """This function iterates through a sequence
    and increments the token frequency of each item
    inputs:
        sequence (list, str, or tuple): sequence of items to count
        tokenfreqs (dict (str, int)): dict mapping items to counts
    returns:
        None. It updates tokenfreqs by reference"""
    ### The instructor solved this in 4 lines
    ### YOUR CODE HERE
    return

def read_linebyline(fname):
    """This function reads in a file line by line
    and updates the word token count
    and character token count
    with each line
    inputs:
        fname (str): name of file to read
        wordfreqs (str, int): count of each word
        charfreqs (str, int): count of each character
    returns:
        dict (str, int): dictionary mapping words to frequencies
        dict (str, int): dictionary mapping chars to frequencies"""
    ### The instructor solved this in 7 lines
    ### YOUR CODE HERE
    return ### YOUR CODE HERE TOO
        
def write_topn(fname, tokenfreqs, topn):
    """This function writes the top n most frequent tokens
    to a file. Each line should be in TOKEN\tCOUNT\n format
    Items should be listed in descending order of frequency
    inputs:
        tokenfreqs (dict (str, int)): dictionary mapping strings to frequencies
        topn (int): The cutoff to use
    returns:
        None"""
    ### The instructor solved this in 4 lines
    ### YOUR CODE HERE
    return

def main():
    # file that data is read from
    infname = "flatland_clean.txt"
    # files that data is written to
    outwordfname = "words_byfreq.txt"
    outcharfname = "chars_byfreq.txt"
    # populate the frequency dictionaries
    wordfreqs, charfreqs = read_linebyline(infname)
    #write the output files
    write_topn(outwordfname, wordfreqs, 100)
    write_topn(outcharfname, charfreqs, 50)
    

if __name__=="__main__":
    main()
