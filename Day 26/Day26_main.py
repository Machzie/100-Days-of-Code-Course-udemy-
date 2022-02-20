# Day 26 Project - NATO Alphabet

import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
letters = alphabet_data.letter.to_list()
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

user_word = input("Please type a word to convert: ").upper()

NATO_list = []
for letter in user_word:
    if letter in letters:
        NATO_list.append(alphabet_dict[letter])

print(NATO_list)
