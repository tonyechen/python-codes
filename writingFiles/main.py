
# text = "Yoooooooo\nThis is some text\nHave a good one!" # changing this will rewrite the file
text = "Will this override?"
with open("test.txt", "w") as file:
    file.write(text)

with open("test.txt", "a") as file:
    file.write(text)

