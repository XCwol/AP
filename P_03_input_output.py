# ask the user for their name
username = input("What is your name?\n")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number?\n"))

# Double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f"\nHi {username}!\nYour favourite number is {fav_num}.\n")

# Output the results of doubling, halving and 
# squaring their favourite integer
print(f"Double {fav_num} is {double}.\n")
print(f"Halve of {fav_num} is {halve}.\n")
print(f"Square {fav_num} is {square}.\n")
