import sys
import os
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

def adfgx_encrypt(**kwargs):
  message = kwargs.get('input',None)
  key1 = kwargs.get('key1',None)
  key2 = kwargs.get('key2',None)

  #makes sure neither key contains duplicate letters

  newkey = []           # create a list for letters
  for i in key1:        # loop through key
    if not i in newkey: # skip duplicates
      newkey.append(i) 
  key1 = ''
  for l in newkey:
    key1 += l  

  newkey = []           # create a list for letters
  for i in key2:        # loop through key
    if not i in newkey: # skip duplicates
      newkey.append(i)  
  key2 = ''
  for l in newkey:
    key2 += l
  
  # should test if file exists
  with open(message) as f:
      plaintext = f.read()

  #set up ADFGX table
  table = AdfgxLookup(key1)
  lookup = table.build_polybius_lookup()

  #cut blanks from plaintext, make all lower case
  #blank cipher text
  plaintext = plaintext.replace(' ','')
  plaintext = plaintext.lower()
  ciphertext = ''

  #set up cipher text
  for letter in plaintext:
    if letter in alphabet:
      ciphertext += lookup[letter.lower()]

  # dictionary for our new matrix
  matrix = {}

  # every letter is a key that points to a list
  for k in key2:
      matrix[k] = []

  # add the message to the each list in a row-wise fashion
  i = 0
  for m in ciphertext:
      matrix[key2[i]].append(m)
      i += 1
      i = i % len(key2)

  print(ciphertext)
  print(matrix)

  temp_matrix = sorted(matrix.items())

  sorted_matrix = {}

  # Rebuild the sorted matrix into a dictionary again
  for item in temp_matrix:
      sorted_matrix[item[0]] = item[1]

  print(sorted_matrix)

  print_message(sorted_matrix, key2)

def adfgx_decrypt(**kwargs):
  message = kwargs.get('input',None)
  key1 = kwargs.get('key1',None)
  key2 = kwargs.get('key2',None)

  #makes sure neither key contains duplicate letters
  newkey = []           # create a list for letters
  for i in key1:        # loop through key
    if not i in newkey: # skip duplicates
      newkey.append(i) 
  key1 = ''
  for l in newkey:
    key1 += l  

  newkey = []           # create a list for letters
  for i in key2:        # loop through key
    if not i in newkey: # skip duplicates
      newkey.append(i)  
  key2 = ''
  for l in newkey:
    key2 += l

  #set up ADFGX table
  table = AdfgxLookup(key1)
  lookup = table.build_polybius_lookup()

  # should test if file exists
  with open(message) as f:
    ciphertext = f.read()
  ciphertext = ciphertext.replace(' ', '')
  plaintext = ''

  #dummy variables for columns and position in string
  pos = 0
  cols = len(key2)

  # get sizes to help calculate matrix column lengths
  key2_length = len(key2)             # length of key
  message_length = len(ciphertext)    # message length 

  # figure out the rows and how many short columns
  rows = math.ceil(float(message_length)/float(key2_length))
  short_cols = key2_length - (message_length%key2_length)

  #establish sorted matrix
  sorted_matrix = {}
  for l in key2:
    sorted_matrix[l] = ''

  i = 0
  for l in ciphertext:
    for k in alphabet:
      if k in key2:
        if k in key2[0:(key2_length-short_cols)]:
          for j in range(rows):
            if i < len(ciphertext):
              sorted_matrix[k] += ciphertext[i]
              i += 1
        else:
          for j in range(rows-1):
            if i < len(ciphertext):
              sorted_matrix[k] += ciphertext[i]
              i += 1
  print(sorted_matrix)

  #for every row, add letter to string
  tempText = ''
  for i in range(rows - 1):
    for l in key2:
      tempText += sorted_matrix[l][i]  
  for i in range(key2_length):
    if len(sorted_matrix[key2[i]]) == rows:
      tempText += sorted_matrix[key2[i]][rows - 1]
  
  print(tempText)

  #cipher text equal to temp string
  ciphertext = tempText

  #set up two more blank strings
  tempPair = ""
  tempMessage = ""

  #for every pair of letters, check to find equivalent in key1, and add lookup key to tempMessage
  for i in range(0, len(ciphertext), 2):
    tempPair += ciphertext[i]
    tempPair += ciphertext[i + 1]
    for k in lookup:
      if lookup[k] == tempPair.upper():
        tempMessage += k
    tempPair = ""

  plaintext = tempMessage
  
  print(plaintext)
  

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs


def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=input_file_name] [key1=keyword1] [key2=keyword2] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=input_file.txt key1=first key2=second op=encrypt\n")
    sys.exit()

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 4 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    key1 = params.get('key1',None)
    key2 = params.get('key2',None)

    if not operation and not infile and not key1 and not key2:
        usage()

    if operation.lower() == 'encrypt':
      adfgx_encrypt(**params)
    elif operation.lower() == 'decrypt':
      adfgx_decrypt(**params)
    else:
      usage()
