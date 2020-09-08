#Code skeleton copied from instructor for frequency analysis. 

import sys
import os
import requests

#Dictionary alphabet
alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    #class initiation
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
    
    #counts number of each letter in text
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    #prints the count of letters
    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    #returns Nth most common letter
    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

#put text to be analyzed into the blank quotes
if __name__=='__main__':
    text = " "

#set F to be a frequency class, perform and print frequency analysis.
print("Calculating frequency...")
F = Frequency()

F.count(text)

F.print()
