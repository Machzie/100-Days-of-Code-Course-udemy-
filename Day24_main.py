# Day 24 Project - Mail Merge Challenge

# Open names file and read contents
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.read().splitlines()

# Open starting letter file and read contents
with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_contents = starting_letter.read()

# Write new contents to a new letter
for name in names_list:
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as new_letter:
        new_letter.write(letter_contents.replace("[name]", name))
