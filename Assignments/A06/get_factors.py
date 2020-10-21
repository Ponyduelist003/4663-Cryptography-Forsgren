import sys
import os
import math

primes = [0] * 1000
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

def factors(num):
  flag = 0
  for i in range(2, (math.ceil(math.sqrt(num)) + 1)):
    if num % i == 0:
      for n in range(1000):
        if primes[n] == 0:
          primes[n] = i
          break
      factors(int(num/i))
      flag = 1
      break
  if flag == 0:
    for n in range(1000):
      if primes[n] == 0:
        primes[n] = num
        break

def get_factors(**kwargs):
  input_file = kwargs.get('input',None)
  file1 = open(input_file, 'r')
  numbers = file1.readlines()
  count = 0
  pos = 0

  for number in numbers:
    value = int(number)
    factors(value)
    print(" ")
    print("Number", (pos + 1), ":", number, "-", end = " ")
    pos += 1
    if primes[0] != 0:
      if primes[1] != 0:
        print("Factors:", end = " ")

    for n in range(1000):
      if primes[n] != 0:
        if primes[n + 1] != 0:
          print(primes[n], "x", end = " ")
        else:
          print(primes[n], end = " ")
        count += 1
    if count == 1:
      print("is prime")
    for n in range(1000):
      primes[n] = 0
    count = 0



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

    get_factors(**params)
