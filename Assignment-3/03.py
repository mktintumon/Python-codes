'''
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
--> "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
'''

string = input("Enter a sentence :\n")

# Split the input string into individual words
words = string.split()

# dictionary to store the word frequency
freq = {}

# Loop through each word and update the word frequency
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort the dictionary keys alphanumerically
sorted_keys = sorted(freq.keys())

# Printing word frequency
print("\nFrequency of the words :")
for key in sorted_keys:
    print(key + ":", freq[key])
