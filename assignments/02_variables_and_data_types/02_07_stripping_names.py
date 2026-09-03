author = "\tThis guy\n"
quote = "To do something is to do a thing"
print(f"{author.title().rstrip()} once said \"{quote}\"")
print()
print(f"{author.title().lstrip()} once said \"{quote}\"")
print()
print(f"{author.title().strip()} once said \"{quote}\"")