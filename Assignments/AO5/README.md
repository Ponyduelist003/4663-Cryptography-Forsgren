## 4663 Assignment 5 - Vigenere Breaking
### Griffin Forsgren
### Description:
Takes a file encrypted via vigenere, finds the key length by using the Index of Coincidence, gets every possible decryption via a dictionary attack, and prints out the first 1000 characters of any decrypted text which it finds sufficiently English. 

### Files:
|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [main.py](./break_vig.py)  | Main python code                                           |
|   2   | [input](./inputfile.txt)   | Sample input text                                          |
|   3   | [output](./output.txt)     | Sample output text                                         |

### Instructions:
Run the code as follows: python3 break_vig.py input=inputfile

### Sources
-Stack Overflow:

  - https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python

-Geeks for Geeks:

  - https://www.geeksforgeeks.org/type-conversion-python

-Programiz:

  - https://www.programiz.com/python-programming/methods/built-in/ord
  
I used the sources to help me with file reading to read in the input and type conversion for the decryption algorithm
