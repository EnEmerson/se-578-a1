#!/usr/bin/python

import sys

# A1 Basic Crypto

cypher = """GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICA 
            CGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCBGCGQOEVSHUNSU
            GKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGB
            SLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAEN
            NSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQ
            GKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKR
            EHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKG
            SZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCA
            USOEGCKGCEUQCGAEUGKCUSZUEBGHSKGEHBCUGERPKHEHKHNSZKGGKAD"""


# Helper methods
def split(word):
    return list(word)


# Shifting letters in python w/ only english letters
# Reference: https://stackoverflow.com/questions/48514673/shift-letters-by-a-certain-value-in-python
def down_shift(s, n):
    return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in s)


def up_shift(s, n):
    return ''.join(chr((ord(char) - 97 + n) % 26 + 97) for char in s)


def decrypt_cypher(cypher_string):
    # 1. convert cypher to a character array (and setup a bunch of other variables)
    cypher_array = split(cypher_string)
    up_shifted_array = []
    down_shifted_array = []
    up_shifted_string = ""
    down_shifted_string = ""
    # 2. for each character in the array:
    for number in range(26):
        for character in cypher_array:
            # a. shift the character between 1 and 26 characters up & print
            up_shifted_char = up_shift()
            up_shifted_array.append(up_shifted_char)
            # b. shift the character between 1 and 26 characters down & print
            down_shifted_char = chr(ord(character) + number)
            down_shifted_array.append(down_shifted_char)
        # 3. put everything back together to form more easily readable strings
        for char in up_shifted_array:
            up_shifted_string += char
        for char in down_shifted_array:
            down_shifted_string += char
        # 4. visually compare each output and see which one forms a sentence!
        print("Cypher with UP key shift of: " + str(number) + "\n")
        print(up_shifted_string + "\n")
        print("\n")
        print("Cypher with DOWN key shift of: " + str(number) + "\n")
        print(down_shifted_string + "\n")
        print("\n")
        # 5. Reset variables for next loop
        up_shifted_array = []
        down_shifted_array = []
        up_shifted_string = ""
        down_shifted_string = ""


# Main method
def main():
    decrypt_cypher(cypher)


if __name__ == "__main__":
    main()
