from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want,hit CTRL-C(^C)")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.Truncate()

print("Now I'm going to ask you for a few lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("I am going to write this to thew file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and Finally we close it")
target.close()
