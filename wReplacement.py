str = input("Wirte a messege: ")
print(str, "You want edit this? ")
choice = input("Yes or No: ")
if choice == "Yes":
    word_to_replace = input("Which Word you want to replace: ")
    new_word = input("Select the new word: ")
    if len(word_to_replace) > 0:
        new_str = str.replace(word_to_replace , new_word)
    print(new_str)

elif choice == "No":
    print("Your Messege: ", str)


    