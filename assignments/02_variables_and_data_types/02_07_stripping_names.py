author = "\tThis guy\n"
quote = "To do something is to do a thing"
print(f"{author.title().rstrip()} once said \"{quote}\"")
print()
print(f"{author.title().lstrip()} once said \"{quote}\"")
print()
print(f"{author.title().strip()} once said \"{quote}\"")

"""
backspace t adds at least a tab's length of space 
backspace n as a new line for the next string to start
.rstrip() removes the whitespace/empty space after a varible
.lstrip() removes the whitespace/empty space before a varible
.strip() removes whitespace/empty spaces from both sides of the varible
"""