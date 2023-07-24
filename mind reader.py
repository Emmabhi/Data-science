dialogue_1 = "Think of any number beetween 1 to 10"
dialogue_2 = "Now Multiply it by 2"
dialogue_3 = "Now add number 4 to it"
dialogue_4 = "Now divide the total by 2"
dialogue_5 = "Now subtract the orginal number from the result"
dialogue_6 = "if I am right then the answer should be number 2"
print(dialogue_1)
dialogue_YN = str(input("Write 'yes' when done:"))
if dialogue_YN == "yes":
    print(dialogue_2)
else:
    dialogue_YN = str(input("Write 'yes' when done:"))
dialogue_YN = str(input("Write 'yes' when done:"))
print(dialogue_3)
dialogue_YN = str(input("Write 'yes' when done:"))
if dialogue_YN == "yes":
    print(dialogue_4)
else:
    dialogue_YN = str(input("Write 'yes' when done:"))
dialogue_YN = str(input("Write 'yes' when done:"))
if dialogue_YN == "yes":
    print(dialogue_5)
else:
    dialogue_YN = str(input("Write 'yes' when done:"))
dialogue_YN = str(input("Write 'yes' when done:"))
if dialogue_YN == "yes":
    print(dialogue_6)
else:
    dialogue_YN = str(input("Write 'yes' when done:"))   
dialogue_YN = str(input("Write 'yes' if i am correct:"))
if dialogue_YN == "yes":
    print("I am a Genius!!!")
else:
    print("Please check your calculation again!")