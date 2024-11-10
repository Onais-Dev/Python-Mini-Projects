"""This Take input from the user and can edit it again by the idx number that user will provde"""

info = list(input("Add Your Information: ").split())
print(info)
ques = input("You want to edit any info: ")
if ques.lower() == "yes":
    idx_num = int((input("On Which index: ")))
    if 0 >= idx_num < len(info):
        new_value = (input("Write a new value: "))
        info[idx_num] = new_value
        print(info)
    else:
        print("This Index is not available ")
else: print("You are good to go!")