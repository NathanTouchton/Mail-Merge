#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("names.txt", mode="r") as file:
    names_list = file.readlines()


for name in names_list:
    with open("starting_letter.txt", mode="r") as file:
        contents = file.read()
        letter = open(f"./finished_letters/Letter for {name}.txt", mode="w+")
        modded_letter_text = contents.replace("[name]", name)
        letter.write(modded_letter_text)
        letter.close()
