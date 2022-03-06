PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as letter:
            letter_to_send = letter.write(new_letter)




