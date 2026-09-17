#this is just a file for quickly testing codes

"""
fruits = ["banana", "melon", "apple", "banana" "apple", "strawberry", "banana"]

print(fruits)
"""

fruits = ["banana", "melon", "apple", "banana" "apple", "strawberry", "banana"]
fruits[1]="duran" 
for(x)in range(len(fruits)): 
    if fruits[x] == "banana":
        fruits[x] = "this is a banana"
        
message=(f"I want to eat {fruits[1]}")
print(message)
print(fruits)


"""
To find in index and replace index
list_name = [insert list of items here]
list_name[#] <- put in number from the list
for(x)in range(len(fruits)):
    if list_name [x] == (the item)
    list_name [x] = (replaced word)
"""

for i in range(1, 1000000):
    print(i)