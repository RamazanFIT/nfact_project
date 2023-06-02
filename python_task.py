file = open("text_for_task.txt", "w")

list_1 = ["my name is Ramazan\n", "Today I want to talk about my family\n\n\n\n\n", "I have 5 members in my family\n\n\n"]


file.writelines(list_1)

file.close()


file = open("text_for_task.txt", "r")


some_text = file.read()

print(some_text)

file.close()

file = open("text_for_task.txt", "r")

some_massive_text = file.readlines()


print(some_massive_text)

file.close()

