#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("Input/Letters/starting_letter.txt", mode="w") as text:
#     letter = text.read()
#     print(letter2)

with open("Input/Letters/starting_letter.txt") as letter:
    contents = letter.readlines()

with open("Input/Names/invited_names.txt") as names:
    names_str = names.read()
    names_lst = names_str.split()

for name in names_lst:
    modified_sentence = contents[0].replace("[name]", f"{name}")
    pathname = f"Output/ReadyToSend/{name}_example.txt"
    with open(pathname, mode="w") as final_letter:
        final_letter.write(modified_sentence+''.join(contents[1:]))
