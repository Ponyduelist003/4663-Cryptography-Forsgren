import sys
import math

alphabet = [chr(x+97) for x in range(26)]

class AdfgxLookup:
    def __init__(self,k=None):
        self.key = self.remove_duplicates(k)

        self.alphabet = [chr(x+97) for x in range(26)]
        self.adfgx = ['A','D','F','G','X']
        self.keylen = 0

        if self.key:
            self.keylen = len(self.key)

        self.polybius = None
        self.lookup = None

    def remove_duplicates(self,key):
        """ Removes duplicate letters from a given key, since they
            will break the encryption.
        """
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey: # skip duplicates
                newkey.append(i)
        
        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)
       

    def build_polybius_string(self,key=None):
        """Builds a string consisting of a keyword + the remaining
           letters of the alphabet. 
        """
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    def build_polybius_lookup(self,key=None):
        """ Builds a lookup dictionary so we can get the two letter pairs for each
            polybius letter. 
        """
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}            # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        row = 0 
        col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for row in range(5):
            for col in range(5):
                i = (5 * row) + col
                self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

        return self.lookup


    def sanity_check(self):
        """ This method lets you look at an actual "matrix" that you built using 
            a keyword. 
        """

        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        row = 0
        col = 0
       
        sys.stdout.write('\n  ')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
        sys.stdout.write('\n')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
            for ll in self.adfgx:
                i = (5 * row) + col
                sys.stdout.write(self.polybius[i]+' ')
                col += 1
            row += 1
            col = 0
            sys.stdout.write("\n")

def print_matrix(matrix,rows):
    """ Print the matrix so we can visually confirm that our
        columnar transposition is actually working
    """
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")

def print_message(matrix,key2word):
    """ Prints the message in a left to right fashion, but reads it from
        the matrix by using fractionated matrix. If you think about it
        we don't even need to swap the columns around, if we alphabatize
        the key2word, then use the alphabetized letters to access the 
        matrix. 
    """
    i = 1
    for k in sorted(key2word):
        for d in matrix[k]:

            print(d,end='')

            # the spaces between every two letters is only for appearance
            if i % 2 == 0:
                print(' ',end='')
            i += 1
    print("")

#set up first key as a Polybius lookup
lookupWord = input("Please enter the Polybius keyword:")
table = AdfgxLookup(lookupWord)
key1 = table.build_polybius_lookup()

#set second key word
shuffleWord = input("Please enter the second keyword (do not choose a word with repeated letters):")
key2 = shuffleWord.upper()

#initialize message, removes spaces, set up a temp
message = input("Please enter the text to be decrypted,no punctuation:")
message = message.replace(' ', '')
tempMessage = ""

#for every letter in message, put polybius lookup into temp
for l in message:
  tempMessage += key1[l.lower()]

#replace message with temp
message = tempMessage

# get sizes to help calculate matrix column lengths
key2_length = len(key2)             # length of key
message_length = len(message)       # message length 

# figure out the rows and how many short columns
rows = math.ceil(float(message_length)/float(key2_length))
short_cols = key2_length - (message_length%key2_length)

# dictionary for our new matrix
matrix = {}

# every letter is a key that points to a list
for k in key2:
    matrix[k] = []

# add the message to the each list in a row-wise fashion
i = 0
for m in message:
    matrix[key2[i]].append(m)
    i += 1
    i = i % len(key2)


#print_matrix(matrix,rows)

# Alphabetize the matrix (not really necessary) if you just
# alphabetize the key2 word and use it to access the dictionary
# in alphabetical order instead. BUT this does stick to the 
# algorithm
temp_matrix = sorted(matrix.items())


print("")

sorted_matrix = {}

# Rebuild the sorted matrix into a dictionary again
for item in temp_matrix:
    sorted_matrix[item[0]] = item[1]

#print the encrypted message
print("Encrypted message:")
print_message(sorted_matrix, key2)

#set a blank string
restoredMessage = ""

#for every letter in unsorted key, for every row, write to string horizontally
for i in range(rows - 1):
  for l in key2:
    restoredMessage += sorted_matrix[l][i]

for l in key2:
  if len(sorted_matrix[l]) == rows:
    restoredMessage += sorted_matrix[l][rows - 1]

#set up two more blank strings
tempPair = ""
tempMessage = ""

#for every pair of letters, check to find equivalent in key1, and add two tempMessage
for i in range(0, len(restoredMessage), 2):
  tempPair += restoredMessage[i]
  tempPair += restoredMessage[i + 1]
  for k in key1:
    if key1[k] == tempPair.upper():
      tempMessage += k
  tempPair = ""

#put tempMessage in restoredMessage
restoredMessage = tempMessage

#print decrypted message
print("Decrypted message:")
print(restoredMessage)
