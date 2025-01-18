input_file = open("Input/Letters/starting_letter.txt")
text = input_file.read()
names = open("Input/Names/invited_names.txt").readlines()
for name in names:
    content = text.replace("[name]", name)
    output_file = open(f"Output/ReadyToSend/{name}.txt", "w")
    output_file.write(content)
    output_file.close()

input_file.close()