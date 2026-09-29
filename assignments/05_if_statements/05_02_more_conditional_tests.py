"""
 Brian Medina

 Writing a if statement for if a certain type of car is in the list
"""
cars = ["subaru", "bmw", "toyota", "ferrari", "all-terrain"]
for car in cars:
  if car.lower() == "bmw":
    print("The car is a BMW")
  if car.upper() != "TOYOTA":
    print("The car is not a Toyota")
  if car.lower() != "bmw" and car.lower() != "toyota":
    print(f"The car is neither a BMW nor a Toyota, it's a {car.title()}")


number_list = [56, 23, 71, 24, 86, 0, 100]
second_numbers_list = [24, 53 ,12, 76, 90, 0]
for i in number_list:
  for j in second_numbers_list:
    if i == j:
      print(f"{i} is equal to {j}")
    if i != j:
      print(f"{i} is not equal to {j}")
    if i >= j:
      print(f"{i} is greater than or equal to {j}")
    if i <= j:
      print(f"{i} is less than or equal to {j}")
    if i == 0 or j == 0:
      print("This is just the number 0")
if 100 in number_list and 100 not in second_numbers_list:
  print("100 is in the first list")