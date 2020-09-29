import sys
import os
import math

alphabet = [chr(x+97) for x in range(26)]

typical_frequency = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
}

class frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.freq_percent = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
            self.freq_percent[l] = 0
    
    def typical(self):
        return typical_frequency

    def clear(self):
      for l in alphabet:
        self.freq[l] = 0
  
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        for k in self.freq_percent:
            self.freq_percent[k] = round(self.freq[k] / len(text),2)
        
        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

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

def break_vig(**kwargs):
  input_file = kwargs.get('input',None)

  with open(input_file) as f:
    ciphertext = f.read()

  ciphertext = ciphertext.replace(' ','')
  ciphertext = ciphertext.lower()

  print(len(ciphertext))

  textFreq = frequency()

  keyLength = 0
  tempIndex = 0
  tempIndex2 = 0
  indexCoincidence = 0
  tempText = ""
  for i in range(2,16):
    for j in range(i):
      for k in range(j, len(ciphertext), i):
        tempText += ciphertext[k]
      textFreq.count(tempText)
      for l in alphabet:
        tempIndex2 += textFreq.freq[l] * (textFreq.freq[l] - 1)
      tempIndex2 = tempIndex2/len(tempText)
      tempIndex2 = tempIndex2/(len(tempText) - 1)
      tempIndex2 = tempIndex2/26
      tempIndex += tempIndex2
      tempIndex2 = 0
      tempText = ""
    tempIndex = tempIndex/i
    if abs(tempIndex - .068) < abs(indexCoincidence -.068):
      indexCoincidence = tempIndex
      keyLength = i
    tempIndex = 0
    textFreq.clear()
  print(keyLength)
  print(ciphertext)

def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=input_file_name]")
    print(f"Example:\n\t python {name} input=input_file.txt \n")
    sys.exit()

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 1 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
      usage()

    infile = params.get('input',None)

    if not infile: 
      usage()

    break_vig(**params)
