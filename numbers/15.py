from sys import argv

filename, User_Name = argv
txt= open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
print("type your filename again")
file_again = input(">")

txt_again=open(file_again)
print(txt_again.read())
