from srs import argv

User_Name, filename = argv
txt= open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
print("type your filename again")
file_again = input(">")

txt_again=open(file_again)
print(txt_again.read())
