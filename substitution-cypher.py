#!/usr/bin/python
import string

# A1 Basic Crypto

cipher = """GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICA 
            CGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCBGCGQOEVSHUNSU
            GKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGB
            SLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAEN
            NSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQ
            GKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKR
            EHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKG
            SZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCA
            USOEGCKGCEUQCGAEUGKCUSZUEBGHSKGEHBCUGERPKHEHKHNSZKGGKAD"""

alphabet = string.ascii_uppercase


# 1. for each character in the array:
for number in range(27):
    shift = 26-number
    shift %= 26
    # 2. shift the character over
    shifted_array = alphabet[shift:] + alphabet[:shift]
    # 3. map alphabet to shifted array
    table = str.maketrans(alphabet, shifted_array)
    # 4. Decrypt the message!
    decrypted = cipher.translate(table)
    # 5. visually examine each output and see which one makes sense
    print("Cypher with key shift of: " + str(number) + "\n")
    print(decrypted + "\n")
    print("\n")
