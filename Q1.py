#!/usr/bin/python
# Reference project: https://github.com/jinjagit/Cryptography/blob/master/python/substitution%20cipher2.py

# A1 Basic Crypto
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
# English letters based on frequency
# Reference: https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
EnglishFreq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
               'V', 'K', 'J', 'X', 'Q', 'Z']
# Encoded message (taken from the A1 assignment pdf)
encoded = """GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICACGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCBGCGQOEVSHUNSU
            GKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGBSLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAEN
            NSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQGKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKR
            EHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKGSZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCA
            USOEGCKGCEUQCGAEUGKCUSZUEBGHSKGEHBCUGERPKHEHKHNSZKGGKAD""".replace(" ", "")  # Strip whitespace
print()
print("Encoded message: " + encoded)

# Utilize letter frequency analysis, similar to 2.3.2 in Information Security by Mark Stamp:
# Initialize a list of 26 zeros, these will represent the frequencies of each letter in EnglishFreq[]
frequency = []
for x in range(0, 26):
    frequency.append(0)

# Count frequency of each letter in message
for x in range(0, len(encoded)):
    for y in range(0, 26):
        # if the encoded letter we're at matches the letter in the alphabet array
        if encoded[x] == alphabet[y]:
            # increase the frequency of that letter by one
            frequency[y] = frequency[y]+1
max_val = max(frequency)

# Duplicate alphabet list to use as a comparator to frequency list
# Sort alphabet based on frequency of appearance in encoded message
frequency_list = alphabet.copy()
n = 0
frequency_test = 0
for x in range(0, max_val + 1):
    frequency_test = max_val - x
    for y in range(0, 26):
        if frequency[y] == frequency_test:
            frequency_list[n] = alphabet[y]
            n = n+1

# Step through message one letter at a time, replacing each letter with its frequency "twin"
decoded = ""
for x in range(0, len(encoded)):
    if encoded[x] != " ":
        for y in range(0, 26):
            if encoded[x] == frequency_list[y]:
                decoded = decoded + EnglishFreq[y]
    else:
        decoded = decoded + " "
print()
print("Partially decoded message: " + decoded)


# Method to take user input for characters to be swapped out manually
def get_char(message):
    error_found = 1
    while error_found == 1:
        char = input(message)
        if len(char) != 1:
            print("ERROR! Input only a single letter")
            error_found = 1
        elif (ord(char) < 65) | ((ord(char) > 90) & (ord(char) < 97)) | (ord(char) > 122):
            print("ERROR! Input only a single letter")
            error_found = 1
        else:
            error_found = 0
    if (ord(char) > 96) & (ord(char) < 123):
        char = chr(ord(char) - 32)
    return char


# Method to replace characters in the partially decoded message
def replace_chars(input_string):
    print()
    identical = 1
    while identical == 1:
        char1 = get_char("input 1st character to switch: ")
        char2 = get_char("input 2nd character to switch 1st with: ")
        if char1 != char2:
            identical = 0
        else:
            print("ERROR! 1st and 2nd characters must be different")
    input_string = input_string.replace(char1, "*")
    input_string = input_string.replace(char2, char1)
    input_string = input_string.replace("*", char2)
    return input_string


# decoded_plus is the decoded message, plus the user's guesses
decoded_plus = decoded
leave = 0
while leave == 0:
    decoded_plus = replace_chars(decoded_plus)
    print()
    print(decoded_plus)
